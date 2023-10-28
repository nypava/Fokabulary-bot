<script>
    export let text;
</script>

<div class="info-container">
    <h1 class="info-icon">i</h1>
    <h1 class="info-text">{text}</h1>
</div>

<style>
    .info-container {
        display: flex;
        width: 100%;
        background-color: var(--tg-theme-bg-color);
        border-radius: 9px;
    }

    .info-text {
        color: var(--tg-theme-text-color);
        line-height: 19px;
        padding: 13px 17px 11px 15px;
        font-size: 15px;
        overflow-wrap: break-word;
        width: 80%;
    }

    .info-icon {
        align-self: center;
        width: 22px;
        height: 22px;
        font-size: 14px;
        line-height: 22px;
        font-weight: 600;
        color: #fff;
        text-align: center;
        background: var(--tg-theme-hint-color);
        padding: 0px 0 0 1px;
        margin-left: 10px;
        border-radius: 11px;
    }
</style>
