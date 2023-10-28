const INEVENTS = ["pointerdown", "touchstart"];
const OUTEVENTS = [
    "pointerup",
    "mouseleave",
    "dragleave",
    "touchmove",
    "touchend",
    "touchcancel",
];
const CLASS = "ripple-effect";
const CENTER_CLASS = "ripple-center";
const addEvent = (el, event, callback) => {
    el.addEventListener(event, callback);
};
const removeEvent = (el, event, callback) => {
    el.removeEventListener(event, callback);
};
const findFurthestPoint = (clickPointX, elementWidth, offsetX, clickPointY, elementHeight, offsetY) => {
    const x = clickPointX - offsetX > elementWidth / 2 ? 0 : elementWidth;
    const y = clickPointY - offsetY > elementHeight / 2 ? 0 : elementHeight;
    const d = Math.hypot(x - (clickPointX - offsetX), y - (clickPointY - offsetY));
    return d;
};
export { INEVENTS, OUTEVENTS, CLASS, CENTER_CLASS, addEvent, removeEvent, findFurthestPoint, };
