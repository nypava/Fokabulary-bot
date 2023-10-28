<script>
    import Sticker from "./components/Sticker.svelte";
    import MainPoint from "./components/MainPoint.svelte";
    import FullInfo from "./components/FullInfo.svelte";
    import { correctStore, } from "./stores/info";
    import { questionStore } from "./stores/question";
    
    let grade;
    let quesions = $questionStore;
    let total_points = $correctStore;

    if (total_points >= quesions.length * 0.9) {
        grade = "excellent";
    } else if (total_points <= quesions.length * 0.2) {
        grade = "bad";
    } else {
        grade = "good";
    }
</script>

<div class="main-container">
    <div class="point-container">
        <MainPoint point={total_points} total_question={quesions.length} />
    </div>
    
    <div class="sticker-container">
        <Sticker {grade} />
    </div>
    
    <div class="fullinfo-container">
        <FullInfo />
    </div>
</div>

<style>
    .fullinfo-container, .point-container {
        margin-left: 3%;
    }

    .sticker-container,
    .point-container {
        display: flex;
        justify-content: center;
    }

    .point-container {
        border-radius: 20px;
        width: 95%;
        margin-top: 1.3em;
        background-color: var(--tg-theme-bg-color);
    }

    .sticker-container {
        margin-top: 3em;
    }

    .fullinfo-container {
        display: flex;
        margin-top: 4em;
        justify-self: center;
        background-color: var(--tg-theme-bg-color);
        border-radius: 10px;
        width: 93%;
    }
</style>
