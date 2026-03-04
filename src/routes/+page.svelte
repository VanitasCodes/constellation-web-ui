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

  function handleCommand(command) {
    console.log('Global:', command);
  }

  function handleSatelliteCommand(name, command) {
    console.log('Satellite:', name, command);
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
