<!-- src/components/HeroGrid.svelte -->
<script lang="ts">
  import type { Hero } from '../types/Hero';

  export let heroes: Hero[] = [];

  $: {
    heroes.forEach(hero => console.log(`Image URL for ${hero.name}:`, hero.portraitURL));
  }
</script>

<style>
  .hero-name {
    text-align: center;
    font-weight: bold;
    margin-bottom: 1rem;
  }
</style>

<div class="grid grid-cols-6 gap-6">
  {#each heroes as hero}
    <div>
      <h3 class="hero-name">{hero.name}</h3>
      <img src="{hero.portraitURL}" alt="{hero.name}" />
    </div>
  {/each}
</div>
