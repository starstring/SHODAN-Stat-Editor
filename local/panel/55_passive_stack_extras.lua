-- local overlay: two Armory Forge ideas for passive stacks, and where their setting lives.
--
-- 1. **Conflicts**: when a stacked passive adds a modifier the target already has, the panel keeps
--    the target's and drops the other. With "strongest" the value further from "no effect" wins
--    (Armory Forge's `conflicts = strongest`; a multiply counts by |log|, everything else by |v|).
--    The rule lives in the host's install step, so the packaged `hostdata.lua` carries it
--    (local/patch_hostdata.py) and the panel hands it the policy through `require('hostdata')`.
--
-- 2. **Every armor**: one stack that follows any armor worn, instead of one stack per passive. It is
--    expanded here, at install time, into every passive's stack.
--
-- Both are set from the stack dialog (two buttons next to Cancel) and stored in `config.txt` as
-- `passive_conflicts strongest` / `passive_every <ids>`. The panel's own loader ignores those lines
-- and its saver rewrites the file from scratch, so this overlay reads them itself and appends them
-- after every save.
--
-- No `local` at this level (upstream's chunk sits at LuaJIT's 200-local limit).
state.sse_cfg = { conflicts = 'stack', every = nil }

;(function()
    -- read our two lines (the panel's loader skipped them)
    local path = config_path()
    local handle = path and io.open(path, 'rb')
    if not handle then return end
    local text = handle:read('*a') or ''
    handle:close()
    for line in text:gmatch('[^\r\n]+') do
        line = line:gsub('#.*$', '')
        local policy = line:match('^%s*passive_conflicts%s+(%a+)')
        if policy then state.sse_cfg.conflicts = (policy == 'strongest') and 'strongest' or 'stack' end
        local ids = line:match('^%s*passive_every%s+([%d,]+)')
        if ids then
            local list = {}
            for id in ids:gmatch('%d+') do list[#list + 1] = tonumber(id) end
            state.sse_cfg.every = #list > 0 and list or nil
        end
    end
end)()

-- append them after the panel writes its config (it rewrites the whole file each time)
state.sse_save_config = save_config
save_config = function()
    state.sse_save_config()
    local path = config_path()
    if not path then return end
    local handle = path and io.open(path, 'ab')
    if not handle then return end
    handle:write('\r\npassive_conflicts ' .. state.sse_cfg.conflicts .. '\r\n')
    if state.sse_cfg.every then
        handle:write('passive_every ' .. table.concat(state.sse_cfg.every, ',') .. '\r\n')
    end
    handle:close()
end

-- the stacks the host installs: the panel's own, plus 'every armor', with the policy handed over
state.sse_stacks = state.stacks
state.stacks = function()
    local base = state.sse_stacks()
    local cfg = state.sse_cfg
    local ok, host = pcall(require, 'hostdata')
    if ok and type(host) == 'table' and host.set_conflicts then host.set_conflicts(cfg.conflicts) end
    if not cfg.every or #cfg.every == 0 then return base end
    local out = {}
    for target, list in pairs(base) do out[target] = list end
    for _, entry in ipairs(weapons) do
        local index = entry.passive and tables[entry.passive] and tables[entry.passive].index
        local id = index and index.id
        if id then
            local list, seen = {}, { [id] = true }
            for _, other in ipairs(base[id] or {}) do
                if not seen[other] then seen[other], list[#list + 1] = true, other end
            end
            for _, other in ipairs(cfg.every) do
                if not seen[other] then seen[other], list[#list + 1] = true, other end
            end
            if #list > 0 then out[id] = list end
        end
    end
    return out
end

-- The two buttons are drawn by the generated panel (local/patch_panel_ui.py): draw() builds its
-- own nested rect/text/button helpers, so an appended overlay can add clickable regions but cannot
-- draw. Their clicks are handled below.

state.sse_click = click
click = function(key)
    local kind = key and key:match('^([%w_]+)')
    if kind == 'pconf' then
        state.sse_cfg.conflicts = state.sse_cfg.conflicts == 'strongest' and 'stack' or 'strongest'
        mark_config_dirty()
        ui.message = { text = 'Modifiers both passives have: ' .. state.sse_cfg.conflicts ..
                             (state.sse_cfg.conflicts == 'strongest' and ' (the stronger value wins)' or
                              ' (the first one is kept)'), till = api.now() + 5 }
        return
    elseif kind == 'pevery' then
        local entry = ui.stack_pick
        local index = entry and entry.passive and tables[entry.passive] and tables[entry.passive].index
        local target = index and index.id
        if state.sse_cfg.every then
            state.sse_cfg.every = nil
        else
            local list = {}
            for _, other in ipairs((target and settings.stacks[target]) or {}) do list[#list + 1] = other end
            if #list == 0 then
                ui.message = { text = 'Add a passive to this armor first: Every armor copies this page\'s stack.',
                               till = api.now() + 5 }
                return
            end
            state.sse_cfg.every = list
        end
        mark_config_dirty()
        ui.message = { text = state.sse_cfg.every and
            ('Every armor: ' .. #state.sse_cfg.every .. ' passive(s) added to all ' .. #weapons ..
             ' passive pages at install') or 'Every armor: off', till = api.now() + 5 }
        return
    end
    return state.sse_click(key)
end

;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local words = ({ ['zh-Hans'] = { '冲突时', '所有护甲', '关闭', '最强值胜出', '保留第一个' },
                         ['zh-Hant'] = { '衝突時', '所有護甲', '關閉', '最強值勝出', '保留第一個' },
                         ['ru'] = { 'Конфликты', 'Вся броня', 'выкл', 'сильнейшее значение', 'первое значение' } })[lang.id]
        if words then
            lang.exact['Conflicts'] = words[1]
            lang.exact['Every armor'] = words[2]
            lang.exact['off'] = lang.exact['off'] or words[3]
            lang.exact['strongest'] = words[4]
            lang.exact['stack'] = words[5]
        end
    end
end)()
