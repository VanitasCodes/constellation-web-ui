<script>
  import HeaderBar from '$lib/components/HeaderBar.svelte';
  import ControlPanel from '$lib/components/ControlPanel.svelte';
  import SatelliteCard from '$lib/components/SatelliteCard.svelte';

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

  function handleCommand(command) {
    let t = transitions[command];
    if (!t) return;

    let suffix = command === 'start' ? ` (Run: ${runId})` : '';

    satellites = satellites.map((sat) => {
      if (t.from.includes(sat.state)) {
        return {
          ...sat,
          state: t.to,
          lastMessage: labels[command] + suffix,
        };
      }
      return sat;
    });
  }

  function handleSatelliteCommand(name, command) {
    let t = transitions[command];
    if (!t) return;

    let suffix = command === 'start' ? ` (Run: ${runId})` : '';

    satellites = satellites.map((sat) => {
      if (sat.name === name && t.from.includes(sat.state)) {
        return {
          ...sat,
          state: t.to,
          lastMessage: labels[command] + suffix,
        };
      }
      return sat;
    });
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
