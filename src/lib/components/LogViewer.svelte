<script>
  let { logs = [], satellites = [], onclear } = $props();

  let levelFilter = $state('ALL');
  let sourceFilter = $state('ALL');
  let searchText = $state('');
  let logContainer;
  let autoScroll = true;

  const levels = [
    'ALL',
    'CRITICAL',
    'WARNING',
    'STATUS',
    'INFO',
    'DEBUG',
    'TRACE',
  ];

  const levelRank = {
    TRACE: 0,
    DEBUG: 1,
    INFO: 2,
    STATUS: 3,
    WARNING: 4,
    CRITICAL: 5,
  };

  let sources = $derived([
    'ALL',
    'Controller',
    ...satellites.map((s) => s.name),
  ]);

  let filtered = $derived.by(() => {
    return logs.filter((log) => {
      if (levelFilter !== 'ALL') {
        if ((levelRank[log.level] ?? 0) < (levelRank[levelFilter] ?? 0))
          return false;
      }
      if (sourceFilter !== 'ALL' && log.source !== sourceFilter) return false;
      if (
        searchText &&
        !log.message.toLowerCase().includes(searchText.toLowerCase())
      )
        return false;
      return true;
    });
  });

  const levelClass = {
    CRITICAL: 'critical',
    STATUS: 'status',
    WARNING: 'warning',
    INFO: 'info',
    DEBUG: 'debug',
    TRACE: 'trace',
  };

  function handleScroll() {
    if (logContainer) {
      let { scrollTop, scrollHeight, clientHeight } = logContainer;
      autoScroll = scrollHeight - scrollTop - clientHeight < 50;
    }
  }

  $effect(() => {
    filtered;
    if (autoScroll && logContainer) {
      logContainer.scrollTop = logContainer.scrollHeight;
    }
  });
</script>

<div class="viewer">
  <div class="toolbar">
    <div class="toolbar-left">
      <select bind:value={levelFilter}>
        {#each levels as lv}
          <option value={lv}>{lv}</option>
        {/each}
      </select>
      <select bind:value={sourceFilter}>
        {#each sources as src}
          <option value={src}>{src}</option>
        {/each}
      </select>
      <input type="text" placeholder="Search logs..." bind:value={searchText} />
    </div>
    <div class="toolbar-right">
      <span class="count">{filtered.length} messages</span>
      <button class="clear-btn" onclick={() => onclear?.()}>Clear</button>
    </div>
  </div>

  <div class="entries" bind:this={logContainer} onscroll={handleScroll}>
    {#each filtered as log}
      <div class="row {levelClass[log.level] ?? 'info'}">
        <span class="time">{log.time}</span>
        <span class="level">{log.level}</span>
        <span class="source">{log.source}</span>
        <span class="msg">{log.message}</span>
      </div>
    {/each}
    {#if filtered.length === 0}
      <div class="empty">No log entries</div>
    {/if}
  </div>
</div>

<style>
  .viewer {
    flex: 1;
    display: flex;
    flex-direction: column;
    background: #1a1b1e;
    min-height: 280px;
    margin: 0 24px 24px;
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid #2c2e33;
  }

  .toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 16px;
    background: #25262b;
    border-bottom: 1px solid #2c2e33;
    gap: 10px;
    flex-wrap: wrap;
  }

  .toolbar-left {
    display: flex;
    gap: 8px;
    align-items: center;
  }

  .toolbar-right {
    display: flex;
    gap: 14px;
    align-items: center;
  }

  select,
  input {
    background: #2c2e33;
    border: 1px solid #373a40;
    color: #c1c2c5;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 12px;
    outline: none;
    transition: border-color 0.15s;
  }

  select:focus,
  input:focus {
    border-color: #4263eb;
  }

  input {
    width: 180px;
    font-family: 'JetBrains Mono', monospace;
  }

  .count {
    font-size: 12px;
    color: #5c636a;
    font-family: 'JetBrains Mono', monospace;
  }

  .clear-btn {
    padding: 4px 14px;
    background: #373a40;
    border: 1px solid #495057;
    color: #c1c2c5;
    border-radius: 4px;
    font-size: 12px;
    cursor: pointer;
    transition: background 0.12s;
  }

  .clear-btn:hover {
    background: #495057;
  }

  .entries {
    flex: 1;
    overflow-y: auto;
    padding: 6px 0;
    max-height: 360px;
  }

  .row {
    display: flex;
    padding: 2px 16px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    line-height: 1.8;
    white-space: nowrap;
  }

  .time {
    min-width: 80px;
    opacity: 0.6;
  }

  .level {
    min-width: 90px;
    font-weight: 600;
  }

  .source {
    min-width: 250px;
    opacity: 0.65;
  }

  .msg {
    flex: 1;
  }

  .critical {
    color: #ff6b6b;
    background: rgba(224, 49, 49, 0.08);
  }
  .status {
    color: #51cf66;
  }
  .warning {
    color: #fcc419;
  }
  .info {
    color: #dee2e6;
  }
  .debug {
    color: #868e96;
  }
  .trace {
    color: #5c636a;
  }

  .empty {
    padding: 32px;
    text-align: center;
    color: #495057;
    font-size: 13px;
  }

  .entries::-webkit-scrollbar {
    width: 6px;
  }
  .entries::-webkit-scrollbar-track {
    background: #1a1b1e;
  }
  .entries::-webkit-scrollbar-thumb {
    background: #373a40;
    border-radius: 3px;
  }
  .entries::-webkit-scrollbar-thumb:hover {
    background: #495057;
  }

  @media (max-width: 768px) {
    .viewer {
      margin: 0 16px 16px;
    }
    .toolbar {
      flex-direction: column;
      align-items: flex-start;
    }
    .source {
      min-width: 160px;
    }
  }
</style>
