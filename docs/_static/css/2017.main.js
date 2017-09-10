import React, {StyleSheet, Dimensions, PixelRatio} from "react-native";
const {width, height, scale} = Dimensions.get("window"),
    vw = width / 100,
    vh = height / 100,
    vmin = Math.min(vw, vh),
    vmax = Math.max(vw, vh);

export default StyleSheet.create({
    "body": {
        "backgroundColor": "#f2f0eb"
    },
    "divnavbar": {
        "marginBottom": 0
    },
    "navnavbar": {
        "marginBottom": 0
    },
    "divnavbar > divcontainer": {
        "width": 700,
        "marginLeft": "auto",
        "marginRight": "auto"
    },
    "divhero divrowrow-logo": {
        "paddingTop": 0,
        "paddingRight": 0,
        "paddingBottom": 0,
        "paddingLeft": 0
    },
    "divhero divhero-logo": {
        "verticalAlign": "center",
        "textAlign": "center"
    },
    "divhero divhero-nav": {
        "textAlign": "left"
    },
    "divhero img": {
        "paddingTop": 50,
        "paddingBottom": 50,
        "width": "100%"
    },
    "divhero-nav": {
        "paddingTop": 50,
        "paddingRight": 40,
        "paddingBottom": 20,
        "paddingLeft": 40,
        "fontSize": 1.3,
        "fontWeight": "100",
        "textTransform": "uppercase",
        "color": "#232321"
    },
    "divhero-nav a": {
        "paddingTop": 0,
        "paddingRight": 0.5,
        "paddingBottom": 0,
        "paddingLeft": 0.5,
        "display": "inline-block"
    },
    "divhero-nav a:link": {
        "color": "#232321"
    },
    "divhero-nav a:visited": {
        "color": "#232321"
    },
    "divhero-nav a:hover": {
        "color": "#ae5739"
    },
    "divhero-nav a:active": {
        "color": "#ae5739"
    },
    "divhero-nav ul": {
        "marginTop": 0.3
    },
    "divhero-nav lihighlight a": {
        "marginTop": 0.2,
        "marginRight": 0,
        "marginBottom": 0.2,
        "marginLeft": 0,
        "fontWeight": "bold",
        "borderRadius": 0.2
    },
    "divhero-nav lihighlight a:link": {
        "backgroundColor": "#ae5739",
        "color": "#ffffef"
    },
    "divhero-nav lihighlight a:visited": {
        "backgroundColor": "#ae5739",
        "color": "#ffffef"
    },
    "divhero-nav lihighlight a:hover": {
        "backgroundColor": "#be6749",
        "color": "#ffffef"
    },
    "divhero-nav lihighlight a:active": {
        "backgroundColor": "#be6749",
        "color": "#ffffef"
    },
    "divhero-nav pinfo": {
        "paddingTop": 1,
        "fontSize": 1
    },
    "divcol-sponsors": {
        "paddingTop": 0
    },
    "h1": {
        "marginTop": 1.5,
        "marginBottom": 0.5,
        "textTransform": "uppercase",
        "fontWeight": "200",
        "color": "#ae5739"
    },
    "h2": {
        "marginTop": 1.5,
        "marginBottom": 0.5,
        "textTransform": "uppercase",
        "fontWeight": "200",
        "color": "#ae5739"
    },
    "h3": {
        "marginTop": 1.5,
        "marginBottom": 0.5,
        "textTransform": "uppercase",
        "fontWeight": "200",
        "color": "#ae5739"
    },
    "h4": {
        "marginTop": 1.5,
        "marginBottom": 0.5,
        "fontWeight": "800",
        "color": "#ae5739"
    },
    "h5": {
        "marginTop": 1.5,
        "marginBottom": 0.5,
        "fontWeight": "800",
        "color": "#ae5739"
    },
    "h6": {
        "marginTop": 1.5,
        "marginBottom": 0.5,
        "fontWeight": "800",
        "color": "#ae5739"
    },
    "p": {
        "marginBottom": 0.5,
        "fontSize": 1.15,
        "lineHeight": 1.5
    },
    "divcol-content ul li": {
        "fontSize": 1.15
    },
    "a:link": {
        "color": "#ae5739"
    },
    "a:visited": {
        "color": "#ae5739"
    },
    "a:hover": {
        "color": "#ae5739"
    },
    "a:active": {
        "color": "#ae5739"
    },
    "aheaderlink": {
        "textDecoration": "none",
        "fontSize": 0.75,
        "lineHeight": 1.5
    },
    "aheaderlink:link": {
        "display": "none"
    },
    "aheaderlink:visited": {
        "display": "none"
    },
    "aheaderlink:active": {
        "display": "none"
    },
    "aheaderlink:hover": {
        "color": "#bbc"
    },
    "table": {
        "fontSize": 1.1,
        "marginTop": 1,
        "marginRight": 2,
        "marginBottom": 1,
        "marginLeft": 2
    },
    "tr": {
        "borderBottom": "1px solid #ccc"
    },
    "tr:first-child": {
        "borderTop": "1px solid #ccc"
    },
    "td": {
        "paddingTop": 0.5,
        "paddingRight": 0.5,
        "paddingBottom": 0.5,
        "paddingLeft": 0.5
    },
    "divfooter": {
        "marginTop": 2,
        "paddingTop": 2,
        "paddingBottom": 2,
        "fontSize": 1.1,
        "lineHeight": 32,
        "background": "#fff"
    },
    "divfooter span": {
        "paddingTop": 0,
        "paddingRight": 0.4,
        "paddingBottom": 0,
        "paddingLeft": 0.4
    },
    "divheader": {
        "background": "#fff"
    },
    "button-tito-writethedocs-write-the-docs-na-2015-1": {
        "marginTop": 0,
        "marginRight": 0,
        "marginBottom": 1,
        "marginLeft": 0,
        "paddingTop": 9,
        "paddingRight": 14,
        "paddingBottom": 9,
        "paddingLeft": 14,
        "border": "none",
        "fontSize": 1.3,
        "fontWeight": "100",
        "textAlign": "center",
        "textTransform": "uppercase",
        "background": "#ab7774",
        "color": "#f2f0eb"
    },
    "button-tito-writethedocs-write-the-docs-na-2015-1:active": {
        "background": "#8b5754"
    },
    "divrow-images": {
        "overflow": "auto",
        "marginTop": 1
    },
    "divrow-images img": {
        "width": "100%",
        "paddingTop": 0.5,
        "paddingRight": 0.5,
        "paddingBottom": 0.5,
        "paddingLeft": 0.5,
        "boxSizing": "border-box",
        "WebkitBoxSizing": "border-box",
        "MozBoxSizing": "border-box",
        "borderRadius": 0.65,
        "WebkitBorderRadius": 0.65,
        "MozBorderRadius": 0.65
    },
    "divclear": {
        "clear": "both"
    },
    "table tdschedule-time": {
        "width": 8,
        "fontWeight": "bold"
    },
    "divrowrow-speaker": {
        "marginTop": 1,
        "clear": "both"
    },
    "divrowrow-speakerrow-speaker-keynote p": {
        "fontSize": 1.1
    },
    "divrowrow-speakerrow-speaker-keynote li": {
        "fontSize": 1.1
    },
    "divrowrow-speaker p": {
        "fontSize": 1
    },
    "divrowrow-speaker li": {
        "fontSize": 1
    },
    "divrowrow-speaker imgspeaker-image": {
        "width": "100%",
        "marginBottom": 1,
        "marginRight": 0,
        "borderRadius": 5,
        "MozBorderRadius": 5,
        "WebkitBorderRadius": 5
    },
    "divrowrow-speaker h1": {
        "paddingTop": 0,
        "marginTop": 0
    },
    "divrowrow-speaker h2": {
        "paddingTop": 0,
        "marginTop": 0
    },
    "divrowrow-speaker h3": {
        "paddingTop": 0,
        "marginTop": 0
    },
    "divrowrow-speaker h4": {
        "paddingTop": 0,
        "marginTop": 0
    },
    "divrowrow-speaker spanspeaker-details": {
        "display": "block",
        "marginTop": 0.3,
        "marginRight": 0,
        "marginBottom": 0.3,
        "marginLeft": 0,
        "fontSize": 0.7,
        "textTransform": "initial"
    },
    "divrowrow-speakers": {
        "marginTop": 1,
        "marginBottom": 1
    },
    "divrowrow-speakers dl > dt": {
        "marginTop": 0.65,
        "fontSize": 1.2
    },
    "divrowrow-speakers dl > dd": {
        "fontStyle": "italic",
        "paddingTop": 0.3,
        "paddingRight": 1,
        "paddingBottom": 0.3,
        "paddingLeft": 1
    },
    "divrow-sponsors > div": {
        "marginTop": 2,
        "textAlign": "center"
    },
    "divinjected": {
        "display": "none"
    },
    "blockquote > div > p": {
        "fontSize": 1
    }
});