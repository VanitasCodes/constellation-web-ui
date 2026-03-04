<script>
  let { satellites = [] } = $props();

  let count = $derived(satellites.length);

  let globalState = $derived.by(() => {
    let states = satellites.map((s) => s.state);
    if (states.includes('ERROR')) return 'ERROR';
    let unique = [...new Set(states)];
    if (unique.length === 1) return unique[0];
    return 'MIXED';
  });

  function dotColor(state) {
    if (state === 'ERROR') return 'red';
    if (state === 'MIXED') return 'yellow';
    return 'green';
  }
</script>

<header>
  <div class="left">
    <h1>Constellation Web Interface</h1>
    <span class="group-tag">test_experiment</span>
  </div>
  <div class="right">
    <span class="sat-count">{count} Satellites</span>
    <div class="indicator">
      <span class="dot {dotColor(globalState)}"></span>
      <span class="indicator-text">{globalState}</span>
    </div>
    <div class="indicator">
      <span class="dot green"></span>
      <span class="indicator-text">Connected</span>
    </div>
  </div>
</header>

<style>
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 24px;
    background: #fff;
    border-bottom: 1px solid #e0e2e6;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04);
  }

  .left {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  h1 {
    font-size: 17px;
    font-weight: 700;
    color: #1a1b1e;
    letter-spacing: -0.3px;
  }

  .group-tag {
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
    color: #6c757d;
    background: #f1f3f5;
    padding: 3px 10px;
    border-radius: 4px;
  }

  .right {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .sat-count {
    font-size: 13px;
    font-weight: 600;
    color: #495057;
  }

  .indicator {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .indicator-text {
    font-size: 12px;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
    color: #495057;
  }

  .dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
  }

  .dot.green {
    background: #37b24d;
    box-shadow: 0 0 6px rgba(55, 178, 77, 0.4);
  }

  .dot.yellow {
    background: #f59f00;
    box-shadow: 0 0 6px rgba(245, 159, 0, 0.4);
  }

  .dot.red {
    background: #e03131;
    box-shadow: 0 0 6px rgba(224, 49, 49, 0.4);
  }

  @media (max-width: 768px) {
    header {
      flex-direction: column;
      gap: 10px;
      padding: 12px 16px;
    }
  }
</style>
