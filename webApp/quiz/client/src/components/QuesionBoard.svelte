<script>
    export let questions;
    export let question;

    $: image = questions[question]["quesion-image"];
    $: question_text = questions[question]["question-text"];

</script>

<h4 class="question-status">Question {question + 1} / {questions.length}</h4>
{#if image}
    <img class="question-image" src={image} alt="quesion-img" />
{/if}
<h1 class="question-text">{question_text}</h1>

<style>
    .question-image {
        display: flex;
        margin-top: 10px;
        object-fit: cover;
        width: 100px;
        border-radius: 10px;
    }

    .question-text {
        color: var(--tg-theme-text-color);
        font-size: 15px;
    }

    .question-status {
        padding: 0px;
        margin-bottom: 0px;
        font-size: 14px;
        opacity: 0.6;
        color: var(--tg-theme-text-color);
    }
</style>
