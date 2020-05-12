#!/usr/bin/node

exports.converter = function (base) {
  return function (valor) {
    return valor.toString(base);
  };
};
