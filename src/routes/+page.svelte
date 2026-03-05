<script>
  import HeaderBar from '$lib/components/HeaderBar.svelte';
  import ControlPanel from '$lib/components/ControlPanel.svelte';
  import SatelliteCard from '$lib/components/SatelliteCard.svelte';
  import LogViewer from '$lib/components/LogViewer.svelte';

  let satellites = $state([
    {
      name: 'Sputnik.One',
      state: 'NEW',
      lastMessage: 'Satellite ready',
      host: '192.168.1.10',
      port: 5001,
    },
    {
      name: 'Sputnik.Two',
      state: 'NEW',
      lastMessage: 'Satellite ready',
      host: '192.168.1.11',
      port: 5002,
    },
    {
      name: 'RandomTransmitter.Sender',
      state: 'NEW',
      lastMessage: 'Satellite ready',
      host: '192.168.1.12',
      port: 5003,
    },
  ]);

  let logs = $state([
    {
      time: '10:30:01',
      level: 'STATUS',
      source: 'Controller',
      message: 'System started',
    },
    {
      time: '10:30:02',
      level: 'INFO',
      source: 'Sputnik.One',
      message: 'Satellite discovered',
    },
    {
      time: '10:30:02',
      level: 'INFO',
      source: 'Sputnik.Two',
      message: 'Satellite discovered',
    },
    {
      time: '10:30:02',
      level: 'INFO',
      source: 'RandomTransmitter.Sender',
      message: 'Satellite discovered',
    },
    {
      time: '10:30:03',
      level: 'STATUS',
      source: 'Controller',
      message: '3 satellites connected',
    },
    {
      time: '10:30:05',
      level: 'DEBUG',
      source: 'Sputnik.One',
      message: 'Heartbeat received',
    },
    {
      time: '10:30:06',
      level: 'WARNING',
      source: 'RandomTransmitter.Sender',
      message: 'Buffer usage at 80%',
    },
  ]);

  let runId = $state('run_001');

  const transitions = {
    initialize: { from: ['NEW', 'ERROR', 'SAFE'], to: 'INIT' },
    launch: { from: ['INIT'], to: 'ORBIT' },
    start: { from: ['ORBIT'], to: 'RUN' },
    stop: { from: ['RUN'], to: 'ORBIT' },
    land: { from: ['ORBIT'], to: 'INIT' },
  };

  const labels = {
    initialize: 'Initialized',
    launch: 'Launched',
    start: 'Started',
    stop: 'Stopped',
    land: 'Landed',
  };

  function now() {
    return new Date().toLocaleTimeString('en-GB', { hour12: false });
  }

  function addLog(level, source, message) {
    logs.push({ time: now(), level, source, message });
    if (logs.length > 200) logs = logs.slice(-200);
  }

  function handleCommand(command) {
    let t = transitions[command];
    if (!t) return;

    let suffix = command === 'start' ? ` (Run: ${runId})` : '';
    let count = 0;

    satellites = satellites.map((sat) => {
      if (t.from.includes(sat.state)) {
        count++;
        addLog('STATUS', sat.name, `${labels[command]} successful${suffix}`);
        return { ...sat, state: t.to, lastMessage: labels[command] + suffix };
      }
      return sat;
    });

    if (count > 0) {
      addLog(
        'STATUS',
        'Controller',
        `${labels[command]} ${count} satellite${count !== 1 ? 's' : ''}${suffix}`
      );
    }
  }

  function handleSatelliteCommand(name, command) {
    let t = transitions[command];
    if (!t) return;

    let suffix = command === 'start' ? ` (Run: ${runId})` : '';

    satellites = satellites.map((sat) => {
      if (sat.name === name && t.from.includes(sat.state)) {
        addLog('STATUS', sat.name, `${labels[command]} successful${suffix}`);
        return { ...sat, state: t.to, lastMessage: labels[command] + suffix };
      }
      return sat;
    });
  }

  function clearLogs() {
    logs = [];
  }
</script>

<div class="app">
  <HeaderBar {satellites} />
  <ControlPanel {satellites} bind:runId oncommand={handleCommand} />

  <main>
    <h2 class="section-title">Satellites</h2>
    <div class="grid">
      {#each satellites as sat (sat.name)}
        <SatelliteCard satellite={sat} oncommand={handleSatelliteCommand} />
      {/each}
    </div>
  </main>

  <LogViewer {logs} {satellites} onclear={clearLogs} />
</div>

<style>
  .app {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    background: #f8f9fa;
  }

  main {
    padding: 20px 24px;
  }

  .section-title {
    font-size: 12px;
    font-weight: 700;
    color: #868e96;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin-bottom: 14px;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 12px;
  }

  @media (max-width: 768px) {
    main {
      padding: 16px;
    }
    .grid {
      grid-template-columns: 1fr;
    }
  }
</style>
