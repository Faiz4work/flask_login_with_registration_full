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
/******/ 	return __webpack_require__(__webpack_require__.s = 9);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./app/assets/es6/pages/mail.js":
/*!**************************************!*\
  !*** ./app/assets/es6/pages/mail.js ***!
  \**************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("class AppMail {\r\n\r\n    static init() {\r\n\r\n        $('.mail-list-row').on('click', (e) => {\r\n            $('.mail-content').addClass('mobile-show-content')\r\n            $('.mail-list').addClass('mobile-hide-list')\r\n        })\r\n\r\n        $('.mail-back').on('click', (e) => {\r\n            $('.mail-content').removeClass('mobile-show-content')\r\n            $('.mail-list').removeClass('mobile-hide-list')\r\n        })\r\n\r\n        $('.panel-toggle').on('click', (e) => {\r\n            $('.column-panel').addClass('is-mobile-active')\r\n        })\r\n        $('.panel-toggle-close').on('click', (e) => {\r\n            $('.column-panel').removeClass('is-mobile-active')\r\n        })\r\n\r\n        $(\"#checkAll\").on('change',function(){\r\n            $('.mail-list-row input[type=\"checkbox\"]').prop('checked',$(this).is(\":checked\"));\r\n        }); \r\n\r\n        $('.mail-content-reply').on('click', (e) => {\r\n            $('.mail-reply').removeClass('d-none')\r\n            $('.mail-content-reply').addClass('d-none')\r\n        })\r\n\r\n        $('.compose').on('click', (e) => {\r\n            $('.mail-compose').removeClass('d-none')\r\n            $('.mail-content').addClass('d-none')\r\n            $('.mail-list').addClass('d-none')\r\n        })\r\n\r\n\r\n        new Quill('#mail-reply', {\r\n            theme: 'snow',\r\n            toolbar: [\r\n                ['bold', 'italic', 'underline', 'strike'],        \r\n                ['blockquote', 'code-block'],\r\n                [{ 'header': 1 }, { 'header': 2 }],               \r\n                [{ 'list': 'ordered'}, { 'list': 'bullet' }],\r\n                [{ 'size': ['small', false, 'large', 'huge'] }],  \r\n                [{ 'align': [] }],\r\n                ['link', 'image']                        \r\n            ]\r\n        });\r\n\r\n        new Quill('#mail-compose', {\r\n            theme: 'snow',\r\n            toolbar: [\r\n                ['bold', 'italic', 'underline', 'strike'],        \r\n                ['blockquote', 'code-block'],\r\n                [{ 'header': 1 }, { 'header': 2 }],               \r\n                [{ 'list': 'ordered'}, { 'list': 'bullet' }],\r\n                [{ 'size': ['small', false, 'large', 'huge'] }],  \r\n                [{ 'align': [] }],\r\n                ['link', 'image']                        \r\n            ]\r\n        });\r\n    }\r\n}\r\n\r\n$(() => { AppMail.init(); });\r\n\r\n\n\n//# sourceURL=webpack:///./app/assets/es6/pages/mail.js?");

/***/ }),

/***/ 9:
/*!********************************************!*\
  !*** multi ./app/assets/es6/pages/mail.js ***!
  \********************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("module.exports = __webpack_require__(/*! C:\\Users\\E\\Desktop\\themeforest selling\\Espire\\v4.0.0\\Espire - Bootstrap Admin Template\\v4.0.0\\html\\demo\\app\\assets\\es6\\pages\\mail.js */\"./app/assets/es6/pages/mail.js\");\n\n\n//# sourceURL=webpack:///multi_./app/assets/es6/pages/mail.js?");

/***/ })

/******/ });