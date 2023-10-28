<script>
  // import dependiecing
  import { createEventDispatcher } from "svelte";
  import { ripple } from "../lib/ripple-effect/ripple";
  import "../lib/ripple-effect/ripple.css";

  export let state;

  // create dispatcher for click event
  let dispatcher = createEventDispatcher();

  function callback(event) {
    // dispatch event as click event
    dispatcher("click");
  }
</script>
{#if !state}
  <button class="next-btn enabled" use:ripple on:click={callback}> Next </button>
{:else}
  <button class="next-btn disabled"> Next </button>
{/if}
<style>
  .next-btn {
    display: block;
    transform: scale();
    width: 6em;
    height: 2.5em;
    border-radius: 25px;
    border: 0;
    background-color: var(--tg-theme-button-color);
    color: var(--tg-theme-button-text-color);
    position: relative;
    overflow: hidden;
    border: none;
    cursor: pointer;
  }
  
  .next-btn.disabled {
    opacity: 0.3;
  }
</style>
