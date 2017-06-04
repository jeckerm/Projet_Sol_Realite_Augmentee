// Auto-generated. Do not edit!

// (in-package projection.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class serviceRequest {
  constructor() {
    this.L = [];
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type serviceRequest
    // Serialize the length for message field [L]
    bufferInfo = _serializer.uint32(obj.L.length, bufferInfo);
    // Serialize message field [L]
    obj.L.forEach((val) => {
      bufferInfo = _serializer.int64(val, bufferInfo);
    });
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type serviceRequest
    let tmp;
    let len;
    let data = new serviceRequest();
    // Deserialize array length for message field [L]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [L]
    data.L = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.int64(buffer);
      data.L[i] = tmp.data;
      buffer = tmp.buffer;
    }
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'projection/serviceRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3c2cc25d6004da2681799b24f2e02ab6';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64[] L
    
    `;
  }

};

class serviceResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type serviceResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type serviceResponse
    let tmp;
    let len;
    let data = new serviceResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'projection/serviceResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

};

module.exports = {
  Request: serviceRequest,
  Response: serviceResponse
};
