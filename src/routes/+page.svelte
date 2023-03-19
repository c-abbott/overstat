<script lang="ts">
  import '../tailwind.css';
  import HeroCard from '../components/HeroCard.svelte';
  import type { Hero } from '../types/Hero';
  import heroStats from '../data/mockHeroStats.json';

  const topHeroes = (role: 'damage' | 'support' | 'tank'): Hero[] => {
  return (heroStats as Hero[])
    .filter((hero: Hero) => hero.role === role)
    .sort((a: Hero, b: Hero) => b.winRate - a.winRate)
    .slice(0, 5);
};
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

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  h2 {
    font-size: 1.75rem;
    font-weight: bold;
    color: #1f2937;
    margin-bottom: 1rem;
  }
</style>

<main>
  <h1>Welcome to Overstat</h1>
  <p>Analyze your Overwatch 2 team compositions and improve your game.</p>

  <div class="container mt-12">
    <h1 class="text-4xl font-bold mb-8">Top 5 Heroes by Win Rate</h1>

    <div class="grid">
      <div>
        <h2>Damage</h2>
        {#each topHeroes('damage') as hero}
          <HeroCard {hero} />
        {/each}
      </div>
      <div>
        <h2>Support</h2>
        {#each topHeroes('support') as hero}
          <HeroCard {hero} />
        {/each}
      </div>
      <div>
        <h2>Tank</h2>
        {#each topHeroes('tank') as hero}
          <HeroCard {hero} />
        {/each}
      </div>
    </div>
  </div>
</main>
