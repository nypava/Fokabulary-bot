<script>
    import '@dotlottie/player-component'
    import { onMount } from 'svelte';

    export let grade;
   
    let stickers = {
        "excellent":"https://lottie.host/7babc624-e380-48ff-9b88-e344031c18be/P8oQYH7IrD.lottie",
        "good":"https://lottie.host/eff0187a-5c58-4a5b-a13a-13e9bb399791/yh2sM5rbNk.lottie",
        "bad":"https://lottie.host/3306aaeb-3ff3-4bb8-9bb3-e300e318eedb/aIUYwc7RCT.lottie"
    };

    let sticker_container;

    onMount(()=>{
        sticker_container.insertAdjacentHTML('beforeend', `<dotlottie-player src="${stickers[grade]}" background="transparent" speed="1" style="width: 200px; height: 200px;" loop autoplay></dotlottie-player>`);
    });

</script>
  
<div class="sticker-container" bind:this = {sticker_container}>

</div>
