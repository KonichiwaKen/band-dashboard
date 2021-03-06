(function () {
  'use strict';

  angular
    .module('band-dash', [
      'band-dash.config',
      'band-dash.authentication',
      'band-dash.layout',
      'band-dash.attendance',
      'band-dash.members',
      'band-dash.utils',
      'ui.router',
      'permission',
      'permission.ui',
      'band-dash.routes',
    ]);

  angular
    .module('band-dash.routes', []);

  angular
    .module('band-dash.config', []);

  angular
    .module('band-dash')
    .run(run);

  run.$inject = ['$http'];

  /**
  * @name run
  * @desc Update xsrf $http headers to align with Django's defaults
  */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
