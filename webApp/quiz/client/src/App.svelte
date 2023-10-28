<script>
    import StartPage from "./StartPage.svelte";
    import QuizPage from "./QuizPage.svelte";
    import ResultPage from "./ResultPage.svelte";

    let current_state = "start";

    /**
     * Change state variable to quiz which makes start page to be render.
     */
    function startQuiz() {
        current_state = "quiz";
    }

    /**
     * Change state variable to finish which makes result page to be render.
     */
    function finishQuiz() {
        current_state = "finish";
    }
</script>

<main>
    {#if current_state == "start"}
        <StartPage on:start={startQuiz} />
    {:else if current_state == "quiz"}
        <QuizPage on:finish={finishQuiz} />
    {:else if current_state == "finish"}
        <ResultPage />
    {/if}
</main>

