import React, {StyleSheet, Dimensions, PixelRatio} from "react-native";
const {width, height, scale} = Dimensions.get("window"),
    vw = width / 100,
    vh = height / 100,
    vmin = Math.min(vw, vh),
    vmax = Math.max(vw, vh);

export default StyleSheet.create({
    "good": {
        "border": "2px dotted",
        "borderColor": "green"
    },
    "bad": {
        "border": "2px dotted",
        "borderColor": "red"
    },
    "divconferences-videos-list": {
        "marginTop": 42
    },
    "divconferences-videos-list h2": {
        "marginBottom": 40,
        "marginTop": 12
    },
    "divconferences-videos-list a": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "divconferences-videos-list a:active": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "divconferences-videos-list a:hover": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "divconferences-videos-list a:link": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "divconferences-videos-list a:visited": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "meetup-detail meetup-video-container": {
        "marginTop": 56
    },
    "meetup-list h2": {
        "fontFamily": "'goudy old style', 'minion pro', 'bell mt', Georgia, 'Hiragino Mincho Pro', serif"
    },
    "meetup-container": {
        "maxWidth": 660,
        "marginRight": "auto",
        "marginLeft": "auto",
        "display": "flex",
        "flexWrap": "wrap"
    },
    "meetup-video-container": {
        "maxWidth": 660,
        "marginRight": "auto",
        "marginLeft": "auto",
        "display": "flex",
        "flexWrap": "wrap"
    },
    "meetup-container meetup": {
        "flex": "0 0 100%"
    },
    "meetup-video-container video": {
        "flex": "0 0 100%"
    },
    "meetup-container a": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "meetup-container a:active": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "meetup-container a:hover": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "meetup-container a:link": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "meetup-container a:visited": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "video a": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "video a:active": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "video a:hover": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "video a:link": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "video a:visited": {
        "color": "#3E4349",
        "textDecoration": "none"
    },
    "meetup-detail breadcrumps": {
        "display": "flex",
        "marginLeft": 0
    },
    "ulsocial-media": {
        "display": "flex",
        "marginLeft": 0
    },
    "ulvideo-info": {
        "display": "flex",
        "marginLeft": 0,
        "flexWrap": "wrap"
    },
    "meetup-detail breadcrumps li": {
        "paddingRight": 6,
        "listStyleType": "none"
    },
    "ulsocial-media li": {
        "paddingRight": 16,
        "listStyleType": "none"
    },
    "ulvideo-info li": {
        "paddingRight": 16,
        "listStyleType": "none"
    },
    "meetup-detail breadcrumps li a": {
        "color": "#3E4349",
        "paddingRight": 8,
        "fontFamily": "Garamond, Georgia, serif"
    },
    "meetup-detail  H1": {
        "fontFamily": "Garamond, Georgia, serif"
    },
    "meetup-detail video i": {
        "fontStyle": "normal",
        "fontWeight": "bold"
    },
    "divabout-container": {
        "display": "flex",
        "justifyContent": "space-between",
        "marginTop": 22
    },
    "meetup-detail about-container h1": {
        "marginBottom": 0
    },
    "social-media-icon": {
        "fontSize": 24
    },
    "social-media": {
        "paddingRight": 20
    },
    "embed-container": {
        "position": "relative",
        "paddingBottom": "56.25%",
        "height": 0,
        "overflow": "hidden",
        "maxWidth": "100%"
    },
    "embed-container iframe": {
        "position": "absolute",
        "top": 0,
        "left": 0,
        "width": "100%",
        "height": "100%"
    },
    "embed-container object": {
        "position": "absolute",
        "top": 0,
        "left": 0,
        "width": "100%",
        "height": "100%"
    },
    "embed-container embed": {
        "position": "absolute",
        "top": 0,
        "left": 0,
        "width": "100%",
        "height": "100%"
    },
    "flex-center": {
        "alignItems": "center",
        "justifyContent": "center"
    },
    "bold": {
        "fontWeight": "800"
    },
    "image": {
        "backgroundPosition": "50% 50%",
        "backgroundSize": "cover",
        "backgroundRepeat": "no-repeat",
        "backgroundColor": "#d7d7d7"
    },
    "image-category": {
        "height": 175.047,
        "width": 340
    },
    "image-grid-element": {
        "height": 133.328,
        "width": 200
    },
    "divtalk section": {
        "display": "flex"
    },
    "divspeaker-sidebar": {
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "flexDirection": "column",
        "paddingRight": 20
    },
    "imgspeaker-pic": {
        "maxWidth": 90,
        "height": "auto"
    }
});