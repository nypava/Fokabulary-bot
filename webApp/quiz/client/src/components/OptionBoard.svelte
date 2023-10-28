<script>
    import { createEventDispatcher } from "svelte";
    let dispatch = createEventDispatcher();

    export let option;
    export let status;
</script>

<button class="choose-btn" on:click={() => { dispatch("click", { option: option });}} >
    {#if status === "none"}
        <div class="option none" />
    {:else if status === "correct"}
        <img class="option correct" src='data:image/svg+xml,%3Csvg height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="%23fff" fill-rule="evenodd"%3E%3Crect height="5.5" rx="1.1" transform="matrix(.70710678 -.70710678 .70710678 .70710678 -6.903479 8.428501)" width="2.2" x="5.622361" y="9.797487"/%3E%3Crect height="11" rx="1.1" transform="matrix(.70710678 .70710678 -.70710678 .70710678 10.937311 -5.071194)" width="2.2" x="10.490128" y="5.166905"/%3E%3C/g%3E%3C/svg%3E' alt="" />
    {:else if status === "wrong"}
        <img class="option wrong" src='data:image/svg+xml,%3Csvg height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"%3E%3Cg fill="%23fff" fill-rule="evenodd"%3E%3Crect height="14" rx="1.1" transform="matrix(.70710678 .70710678 -.70710678 .70710678 10.020458 -4.15061)" width="2.2" x="8.920458" y="3.020458"/%3E%3Crect height="14" rx="1.1" transform="matrix(-.70710678 .70710678 .70710678 .70710678 10.020458 -4.15061)" width="2.2" x="8.920458" y="3.020458"/%3E%3C/g%3E%3C/svg%3E' alt="" />
    {/if}

    <p class="choose-text">{option}</p>
</button>

<style>
    .choose-btn {
        background: transparent;
        border-radius: 5px;
        border: transparent;
        width: 20em;
        display: flex;
        align-items: center;
        margin: 0px;
    }

    .choose-text {
        margin: 7px;
        padding-left: 3px;
        font-size: 15px;
        font-weight: 300;
    }
    
    .option {
        border-radius: 11px;
        border: solid var(--tg-theme-text-color) 1.5px;
    }

    .wrong {
        border: none;
        background-color: red;
    }
    .wrong,
    .correct {
        width: 19px;
        height: 19px;
    }
    .none {
        width: 17px;
        height: 17px;
    }
    .correct {
        border: none;
        background-color: #2392e7;
    }
</style>
