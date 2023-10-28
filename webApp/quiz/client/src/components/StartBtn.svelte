<script>
  // import dependiecing
  import { createEventDispatcher } from "svelte";
  import { ripple } from "../lib/ripple-effect/ripple";

  // Import stying css
  import "../styles/shinny.css";
  import "../lib/ripple-effect/ripple.css";

  // create dispatcher for click event
  let dispatcher = createEventDispatcher();

  function callback(event) {
    // dispatch event as click event
    dispatcher("click");
  }
</script>

<button class="start-btn shinny" use:ripple on:click={callback}> Start Quiz</button>

<style>
  .start-btn {
    display: block;
    width: 9em;
    height: 3.1em;
    border-radius: 25px;
    border: 0;
    background-color: var(--tg-theme-button-color);
    color: var(--tg-theme-button-text-color);
    overflow: hidden;
    border: none;
    cursor: pointer;
  }
</style>
