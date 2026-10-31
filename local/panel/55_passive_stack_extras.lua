-- local overlay: where this fork's armor-passive policy is read and saved.
--
-- The policy itself (what a modifier that both passives have does) lives in the host's install step:
-- `local/patch_hostdata.py` patches `append_mods` and adds `M.set_conflicts`, and the packaged
-- `app/hostdata.lua` carries it. This overlay reads the choice from `config.txt`
-- (`passive_conflicts strongest`), hands it to the host before every install, and appends the line
-- again after each save (the panel's own loader ignores it and its saver rewrites the file).
--
-- The "Every armor" list is no longer kept here: upstream gives each armor its own passive list
-- (`settings.armor_passives`), so 60_armor_pages.lua makes "Every armor" an armor page of its own.
--
-- No `local` at this level (upstream's chunk sits at LuaJIT's 200-local limit).
state.sse_cfg = { conflicts = 'stack' }

;(function()
    local path = config_path()
    local handle = path and io.open(path, 'rb')
    if not handle then return end
    local text = handle:read('*a') or ''
    handle:close()
    for line in text:gmatch('[^\r\n]+') do
        line = line:gsub('#.*$', '')
        local policy = line:match('^%s*passive_conflicts%s+(%a+)')
        if policy then state.sse_cfg.conflicts = (policy == 'strongest') and 'strongest' or 'stack' end
    end
end)()

-- append it after the panel writes its config (it rewrites the whole file each time)
state.sse_save_config = save_config
save_config = function()
    state.sse_save_config()
    local path = config_path()
    local handle = path and io.open(path, 'ab')
    if not handle then return end
    handle:write('\r\npassive_conflicts ' .. state.sse_cfg.conflicts .. '\r\n')
    handle:close()
end

-- the policy, handed to the host's install step before it merges each armor's passive list
state.sse_armor_passives_policy = state.armor_passives
state.armor_passives = function()
    local ok, host = pcall(require, 'hostdata')
    if ok and type(host) == 'table' and host.set_conflicts then host.set_conflicts(state.sse_cfg.conflicts) end
    return state.sse_armor_passives_policy()
end

;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local words = ({ ['zh-Hans'] = { '冲突时', '最强值胜出', '保留第一个' },
                         ['zh-Hant'] = { '衝突時', '最強值勝出', '保留第一個' },
                         ['ru'] = { 'Конфликты', 'сильнейшее значение', 'первое значение' } })[lang.id]
        if words then
            lang.exact['Conflicts'] = words[1]
            lang.exact['strongest'] = words[2]
            lang.exact['stack'] = words[3]
        end
    end
end)()
