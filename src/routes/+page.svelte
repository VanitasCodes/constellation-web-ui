<script>
  import HeaderBar from '$lib/components/HeaderBar.svelte';
  import ControlPanel from '$lib/components/ControlPanel.svelte';

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
    console.log('Command:', command);
  }
</script>

<div class="app">
  <HeaderBar {satellites} />
  <ControlPanel {satellites} bind:runId oncommand={handleCommand} />
</div>

<style>
  .app {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    background: #f8f9fa;
  }
</style>
