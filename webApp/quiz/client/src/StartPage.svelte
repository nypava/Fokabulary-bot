<script>
    // Import components
    import { createEventDispatcher } from "svelte";
    import StartBtn from "./components/StartBtn.svelte";
    import { questionStore, titleStore } from "./stores/question";
    import { onMount } from "svelte";

    let server_url = "https://fokabulary-quiz-api.vercel.app";

    onMount(async () => {
        let quiz = await fetch(server_url + "/quizes");
        let quiz_json = await quiz.json();
        questionStore.set(quiz_json["questions"]);
        titleStore.set(quiz_json["title"]);
    });

    // @ts-ignore
    const telegramWebApp = window.Telegram.WebApp;

    // Intiate webapp and expand webapp when it is opened
    telegramWebApp.ready();
    telegramWebApp.expand();

    /**
     * Handler start when start button clicked
     */
    function startHandler() {
        /**
         * Ask the user to confirm that he is not clicked start button unintentionally via pop up.
         */
        telegramWebApp.showConfirm(
            "Are you sure to start the quiz?",
            (event) => {
                if (event) dispatcher("start");
            }
        );
    }

    let dispatcher = createEventDispatcher();
</script>

<div class="start-container">
    <StartBtn on:click={startHandler} />
</div>

<style>
    .start-container {
        position: fixed;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }
</style>
