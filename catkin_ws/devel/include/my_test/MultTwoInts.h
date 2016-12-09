// Generated by gencpp from file my_test/MultTwoInts.msg
// DO NOT EDIT!


#ifndef MY_TEST_MESSAGE_MULTTWOINTS_H
#define MY_TEST_MESSAGE_MULTTWOINTS_H

#include <ros/service_traits.h>


#include <my_test/MultTwoIntsRequest.h>
#include <my_test/MultTwoIntsResponse.h>


namespace my_test
{

struct MultTwoInts
{

typedef MultTwoIntsRequest Request;
typedef MultTwoIntsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MultTwoInts
} // namespace my_test


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::my_test::MultTwoInts > {
  static const char* value()
  {
    return "6a2e34150c00229791cc89ff309fff21";
  }

  static const char* value(const ::my_test::MultTwoInts&) { return value(); }
};

template<>
struct DataType< ::my_test::MultTwoInts > {
  static const char* value()
  {
    return "my_test/MultTwoInts";
  }

  static const char* value(const ::my_test::MultTwoInts&) { return value(); }
};


// service_traits::MD5Sum< ::my_test::MultTwoIntsRequest> should match 
// service_traits::MD5Sum< ::my_test::MultTwoInts > 
template<>
struct MD5Sum< ::my_test::MultTwoIntsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::my_test::MultTwoInts >::value();
  }
  static const char* value(const ::my_test::MultTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::my_test::MultTwoIntsRequest> should match 
// service_traits::DataType< ::my_test::MultTwoInts > 
template<>
struct DataType< ::my_test::MultTwoIntsRequest>
{
  static const char* value()
  {
    return DataType< ::my_test::MultTwoInts >::value();
  }
  static const char* value(const ::my_test::MultTwoIntsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::my_test::MultTwoIntsResponse> should match 
// service_traits::MD5Sum< ::my_test::MultTwoInts > 
template<>
struct MD5Sum< ::my_test::MultTwoIntsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::my_test::MultTwoInts >::value();
  }
  static const char* value(const ::my_test::MultTwoIntsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::my_test::MultTwoIntsResponse> should match 
// service_traits::DataType< ::my_test::MultTwoInts > 
template<>
struct DataType< ::my_test::MultTwoIntsResponse>
{
  static const char* value()
  {
    return DataType< ::my_test::MultTwoInts >::value();
  }
  static const char* value(const ::my_test::MultTwoIntsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MY_TEST_MESSAGE_MULTTWOINTS_H
