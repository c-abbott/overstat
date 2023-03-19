<script lang="ts">
  import type { Hero } from '../types/Hero';
  export let hero: Hero;
</script>

<div class="bg-white shadow-md rounded p-4 m-2 flex items-center">
  <div class="font-bold text-lg">{hero.name}</div>
  <div class="ml-auto">
    Win Rate: <span class="font-semibold">{hero.winRate}%</span>
  </div>
</div>
