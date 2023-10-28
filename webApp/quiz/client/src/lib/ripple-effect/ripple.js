import { INEVENTS, OUTEVENTS, CLASS, CENTER_CLASS, addEvent, removeEvent, findFurthestPoint, } from "./constants";
function ripple(el, options) {
    const addClassIfMissing = () => {
        if (!el.classList.contains(CLASS)) {
            el.classList.add(CLASS);
        }
        if (options?.center) {
            el.classList.add(CENTER_CLASS);
        }
    };
    addClassIfMissing();
    let maximumRadius = 0;
    const setOptions = (options) => {

        if (options?.color) {
            el.style.setProperty("--ripple-color", options.color);
        }

        if (options?.duration) {
            el.style.setProperty("--ripple-duration", options.duration + "s");
        }

        if (options?.maxRadius) {
            maximumRadius = options.maxRadius;
        }
    };
    setOptions(options);
    const createRipple = (e) => {
        addClassIfMissing();
        const rect = el.getBoundingClientRect();
        const radius = findFurthestPoint(e.clientX, el.offsetWidth, rect.left, e.clientY, el.offsetHeight, rect.top);
        const ripple = document.createElement("div");
        ripple.classList.add("ripple");
        let size = radius * 2;
        let top = e.clientY - rect.top - radius;
        let left = e.clientX - rect.left - radius;
        if (maximumRadius && size > maximumRadius) {
            size = maximumRadius * 2;
            top = e.clientY - rect.top - maximumRadius;
            left = e.clientX - rect.left - maximumRadius;
        }
        ripple.style.left = left + "px";
        ripple.style.top = top + "px";
        ripple.style.width = ripple.style.height = size + "px";
        el.appendChild(ripple);
        const removeRipple = () => {
            if (ripple !== null) {
                ripple.style.opacity = "0";
                setTimeout(() => {
                    ripple.remove();
                }, options?.duration ? options.duration * 1000 : 1000);
            }
        };
        OUTEVENTS.forEach((event) => {
            addEvent(el, event, removeRipple);
        });
    };
    INEVENTS.forEach((event) => {
        addEvent(el, event, createRipple);
    });
    return {
        destroy: () => {
            INEVENTS.forEach((event) => {
                removeEvent(el, event, createRipple);
            });
        },
        update: (newOptions) => {
            options = newOptions;
            setOptions(newOptions);
        },
    };
}

export { ripple };
