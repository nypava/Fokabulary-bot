<script>
    export let point;
    export let total_question;
</script>

<div class="point-question-container">
    <h1 class="point">{point}</h1>
    <h1 class="total-question">/{total_question} <span class="pts">pts</span>
    </h1>
</div>

<style>
    .point-question-container {
        display: flex;
        align-items: baseline;
    }

    .point {
        margin: 0;
        font-size: 70px;
        color: var(--tg-theme-link-color);
    }

    .pts {
        color: var(--tg-theme-hint-color);
    }

    .total-question {
        color: var(--tg-theme-text-color);
    }

    .total-question,
    .pts {
        padding-left: 4px;
        font-size: 30px;
    }
</style>
