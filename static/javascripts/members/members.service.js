/**
* Members
* @namespace band-dash.members
*/
(function () {
  'use strict';

  angular
    .module('band-dash.members')
    .factory('Members', Members);

  Members.$inject = ['$http'];

  /**
  * @namespace Members
  * @returns {Factory}
  */
  function Members($http) {
    /**
    * @name Members
    * @desc The Factory to be returned
    */
    var Members = {
      createBand: createBand,
      editMember: editMember,
    };

    return Members;

    ////////////////////

    /**
    * @name createBand
    * @desc Try to create a new band
    * @param {string} identifier The band identifier entered by the user
    * @returns {Promise}
    * @memberOf band-dash.members.Members
    */
    function createBand(identifier) {
      return $http.post('/api/v1/members/band/', {
        identifier: identifier
      });
    }

    function editMember(member) {
      return $http.patch('/api/v1/members/' + member.id + '/', {
        instrument_number: member.instrument_number,
        section: member.section,
      });
    }
  }
})();
