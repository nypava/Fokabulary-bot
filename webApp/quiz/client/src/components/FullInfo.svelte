<script>
    import {
        timeStore,
        correctStore,
        wrongStore,
        missedStore,
    } from "../stores/info";

    let minutes = Math.floor($timeStore / 60);
    let seconds = Math.floor($timeStore - minutes * 60);
</script>

<div>
    <h1 class="correct">
        <img src="https://t.me/img/emoji/40/E29C85.png" alt="correct" /> Correct - {$correctStore}
    </h1>
    <h1 class="wrong">
        <img src="https://t.me/img/emoji/40/E29D8C.png" alt="correct" /> Wrong - {$wrongStore}
    </h1>
    <h1 class="missed">
        <img src="https://t.me/img/emoji/40/E28C9B.png" alt="correct" /> Missed - {$missedStore}
    </h1>
    <h1 class="time">
        <img src="https://t.me/img/emoji/40/E28FB1.png" alt="correct" /> Time -  {String(minutes).length === 1 ? `0${minutes}` : minutes} : {String(seconds).length === 1? `0${seconds}`: seconds}
    </h1>
</div>


<style>
    h1 {
        display: flex;
        align-items: center;
        color: var(--tg-theme-text-color);
        font-size: 18px;
        gap: 5px;
        margin-left: 1em;
    }
    img {
        width: 20px;
    }
</style>
