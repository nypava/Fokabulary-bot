<script>
    // Import components, store, function
    
    import OptionBoard from "./components/OptionBoard.svelte";
    import QuesionBoard from "./components/QuesionBoard.svelte";
    import Time from "./components/Time.svelte";
    import NextBtn from "./components/NextBtn.svelte";
    import InfoText from "./components/InfoText.svelte";
    import { createEventDispatcher } from "svelte";
    import { questionStore } from "./stores/question";
    import {
        timeStore,
        correctStore,
        wrongStore,
        missedStore,
    } from "./stores/info";


    // @ts-ignore
    // Assign telegram object to variable
    const telegramWebApp = window.Telegram.WebApp;

    /**
     * Using telegram objects to hepatic feedback
     * wrong_notitication for wrong option notification (notificationOccured("error"))
     * correct_notification for correct option notification
     */
    const wrong_notification = () => {
        telegramWebApp.HapticFeedback.notificationOccurred("error");
    };
    const correct_notification = () => {
        telegramWebApp.HapticFeedback.notificationOccurred("success");
    };

    // Telgram button (Main button) at the buttom of WebApp
    let main_button = telegramWebApp.MainButton;

    // Change WebApp main button color to red and text to 'Terminate'
    main_button.color = "#ff0000";
    main_button.text = "Terminate";

    // Show the main button and when it click call close function
    main_button.show();
    main_button.onClick(() => {
        telegramWebApp.close();
    });

    // Intial variables
    let questions = $questionStore;
    let current_question = 0;

    let quiz_state = true;
    let wrong_answer = "";

    /**
     * Increase index variable when user click next button.
     */
    function increaseIndex() {
        if (current_question + 1 === questions.length) {
            dispatcher("finish");
            return;
        }
        current_question += 1;
        quiz_state = true;
    }

    /**
     * Check user answer to the correct answer.
     * @param event
     */
    function checkAnswer(event) {
        quiz_state = false;

        // if the answer is correct
        if (event.detail.option == correct_option) {
            correctStore.update((n) => n + 1);
            timeStore.update((n) => n + (questions[current_question]["time"] - time)); // if user missed the question doesn't update else update.
            correct_notification();
        } else {
            wrongStore.update((n) => n + 1);
            timeStore.update((n) => n + (questions[current_question]["time"] - time) )
            wrong_answer = event.detail.option;
            wrong_notification();
        }
    }

    // Variables that depends on the given quesion dataset
    $: current_options = questions[current_question]["options"];
    $: correct_option = questions[current_question]["correct-option"];
    $: description = questions[current_question]["description"];
    $: time = questions[current_question]["time"];

    // Variables that used for displaying timer.
    $: minutes = Math.floor(time / 60);
    $: seconds = Math.floor(time - minutes * 60);

    /**
     * Time interval to decrease time variable.
     */
    setInterval(() => {
        if (time > 0 && quiz_state) time--;
    }, 1000);

    // When time variable become 0 the quiz state becomes false
    $: {
        if (time == 0) {
            quiz_state = false;
            missedStore.update((n) => n + 1);
        }
    }

    let dispatcher = createEventDispatcher();
</script>

<div class="question-container">
    <QuesionBoard {questions} question={current_question} />
</div>

<div class="options-container">
    {#if quiz_state}
        {#each current_options as current_option}
            <div class="option-container">
                <OptionBoard
                    option={current_option}
                    on:click={checkAnswer}
                    status="none"
                />
            </div>
        {/each}
    {:else}
        {#each current_options as current_option}
            {#if current_option == correct_option}
                <div class="option-container">
                    <OptionBoard option={current_option} status="correct" />
                </div>
            {:else if current_option == wrong_answer}
                <div class="option-container">
                    <OptionBoard option={current_option} status="wrong" />
                </div>
            {:else}
                <div class="option-container">
                    <OptionBoard option={current_option} status="none" />
                </div>
            {/if}
        {/each}
    {/if}
</div>

<div class="next-time-container">
    <div class="next-container">
        <NextBtn state={quiz_state} on:click={increaseIndex} />
    </div>

    <div class="time-container">
        <Time {time} {seconds} {minutes} />
    </div>
</div>

<div class="answer-info-container">
    {#if !quiz_state}
        <InfoText text={description} />
    {/if}
</div>

<style>
    .next-time-container,
    .options-container,
    .next-container,
    .question-container {
        margin-left: 0.5em;
        margin-right: 0.5em;
    }

    .next-time-container {
        display: flex;
        align-items: center;
        margin-top: 30px;
    }

    .question-container {
        margin-top: 1em;
        display: inline-block;
    }

    .option-container {
        margin-bottom: 0.2em;
    }

    .time-container {
        margin-left: 2em;
        display: flex;
        gap: 10px;
    }

    .answer-info-container {
        padding-top: 1em;
    }
</style>
