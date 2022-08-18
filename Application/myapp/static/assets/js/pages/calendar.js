/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 1);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./app/assets/es6/pages/calendar.js":
/*!******************************************!*\
  !*** ./app/assets/es6/pages/calendar.js ***!
  \******************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("class Calendar {\r\n\r\n    static init() {\r\n        const calendarEl = document.getElementById('calendar');\r\n\r\n        const calendar = new FullCalendar.Calendar(calendarEl, {\r\n            contentHeight: 700,\r\n            initialDate: '2020-09-12',\r\n            headerToolbar: {\r\n                start: 'title',\r\n                right: 'dayGridMonth,timeGridWeek,timeGridDay'\r\n            },\r\n            editable: true,\r\n            selectable: true,\r\n            businessHours: true,\r\n            dayMaxEvents: true, // allow \"more\" link when too many events\r\n            events: [\r\n                {\r\n                    title: 'All Day Event',\r\n                    start: '2020-09-01'\r\n                },\r\n                {\r\n                    title: 'Long Event',\r\n                    start: '2020-09-07',\r\n                    end: '2020-09-10'\r\n                },\r\n                {\r\n                    groupId: 999,\r\n                    title: 'Repeating Event',\r\n                    start: '2020-09-09T16:00:00',\r\n                    backgroundColor: '#ef2733'\r\n                },\r\n                {\r\n                    groupId: 999,\r\n                    title: 'Repeating Event',\r\n                    start: '2020-09-16T16:00:00',\r\n                    backgroundColor: '#ef2733'\r\n                },\r\n                {\r\n                    title: 'Conference',\r\n                    start: '2020-09-11',\r\n                    end: '2020-09-13'\r\n                },\r\n                {\r\n                    title: 'Meeting',\r\n                    start: '2020-09-12T10:30:00',\r\n                    end: '2020-09-12T12:30:00',\r\n                    backgroundColor: '#ff8911'\r\n                },\r\n                {\r\n                    title: 'Lunch',\r\n                    start: '2020-09-12T12:00:00'\r\n                },\r\n                {\r\n                    title: 'Meeting',\r\n                    start: '2020-09-12T14:30:00'\r\n                },\r\n                {\r\n                    title: 'Happy Hour',\r\n                    start: '2020-09-12T17:30:00'\r\n                },\r\n                {\r\n                    title: 'Dinner',\r\n                    start: '2020-09-12T20:00:00'\r\n                },\r\n                {\r\n                    title: 'Birthday Party',\r\n                    start: '2020-09-13T07:00:00'\r\n                },\r\n                {\r\n                    title: 'Click for Google',\r\n                    url: 'http://google.com/',\r\n                    start: '2020-09-28'\r\n                }\r\n            ]\r\n        });\r\n\r\n        calendar.render();\r\n    }\r\n}\r\n\r\n$(() => { Calendar.init(); });\r\n\r\n\n\n//# sourceURL=webpack:///./app/assets/es6/pages/calendar.js?");

/***/ }),

/***/ 1:
/*!************************************************!*\
  !*** multi ./app/assets/es6/pages/calendar.js ***!
  \************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("module.exports = __webpack_require__(/*! C:\\Users\\E\\Desktop\\themeforest selling\\Espire\\v4.0.0\\Espire - Bootstrap Admin Template\\v4.0.0\\html\\demo\\app\\assets\\es6\\pages\\calendar.js */\"./app/assets/es6/pages/calendar.js\");\n\n\n//# sourceURL=webpack:///multi_./app/assets/es6/pages/calendar.js?");

/***/ })

/******/ });