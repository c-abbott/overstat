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
  /* Your CSS styles go here */
  h1 {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
  }

  p {
    font-size: 1.25rem;
    text-align: center;
  }
</style>

<main>
  <div class="container mx-auto">
    <h1 class="text-2xl font-bold mb-8">Top 5 Heroes by Win Rate</h1>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      <div>
        <h2 class="text-xl font-semibold mb-4">Damage</h2>
        {#each topHeroes('damage') as hero}
          <HeroCard {hero} />
        {/each}
      </div>
      <div>
        <h2 class="text-xl font-semibold mb-4">Support</h2>
        {#each topHeroes('support') as hero}
          <HeroCard {hero} />
        {/each}
      </div>
      <div>
        <h2 class="text-xl font-semibold mb-4">Tank</h2>
        {#each topHeroes('tank') as hero}
          <HeroCard {hero} />
        {/each}
      </div>
    </div>
  </div>
</main>
