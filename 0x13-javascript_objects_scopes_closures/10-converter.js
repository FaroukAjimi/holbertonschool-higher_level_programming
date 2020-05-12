#!/usr/bin/node
exports.converter = function (base) {
  function convertToBase (Base) { return Base.toString(base); }
  return convertToBase;
};
