<script lang="ts">
  import { onMount } from 'svelte';
  import '../tailwind.css';
  import HeroGrid from '../components/HeroGrid.svelte';
  import { getHeroes } from '../overFastApiClient';
  import type { Hero } from '../types/Hero';
  
  let heroes: Hero[] = [];


  onMount(async () => {
    const data = await getHeroes();
    heroes = data.sort((a, b) => a.name.localeCompare(b.name));
  });

</script>

<style>
  main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  h1 {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
    color: #111827;
  }

  p {
    font-size: 1.25rem;
    text-align: center;
    color: #374151;
  }

  .container {
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 2rem;
  }
</style>

<main>
  <h1>Welcome to Overstat</h1>
  <p>Analyze your Overwatch 2 team compositions and improve your game.</p>

  <div class="container mt-12">
    <h1 class="text-4xl font-bold mb-8">Overwatch Heroes</h1>
    <HeroGrid {heroes} />
  </div>
</main>
