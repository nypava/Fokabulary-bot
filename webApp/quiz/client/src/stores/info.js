import { writable } from "svelte/store";


export const timeStore = writable(0);
export const correctStore = writable(0);
export const wrongStore = writable(0);
export const missedStore = writable(0);
