// Generated by gencpp from file candybot_vr/VisionMessage.msg
// DO NOT EDIT!


#ifndef CANDYBOT_VR_MESSAGE_VISIONMESSAGE_H
#define CANDYBOT_VR_MESSAGE_VISIONMESSAGE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace candybot_vr
{
template <class ContainerAllocator>
struct VisionMessage_
{
  typedef VisionMessage_<ContainerAllocator> Type;

  VisionMessage_()
    : face_count(0)
    , smile(false)  {
    }
  VisionMessage_(const ContainerAllocator& _alloc)
    : face_count(0)
    , smile(false)  {
  (void)_alloc;
    }



   typedef int32_t _face_count_type;
  _face_count_type face_count;

   typedef uint8_t _smile_type;
  _smile_type smile;




  typedef boost::shared_ptr< ::candybot_vr::VisionMessage_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::candybot_vr::VisionMessage_<ContainerAllocator> const> ConstPtr;

}; // struct VisionMessage_

typedef ::candybot_vr::VisionMessage_<std::allocator<void> > VisionMessage;

typedef boost::shared_ptr< ::candybot_vr::VisionMessage > VisionMessagePtr;
typedef boost::shared_ptr< ::candybot_vr::VisionMessage const> VisionMessageConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::candybot_vr::VisionMessage_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::candybot_vr::VisionMessage_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace candybot_vr

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'candybot_vr': ['/home/alex/catkin_ws/src/candybot_vr/msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::candybot_vr::VisionMessage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::candybot_vr::VisionMessage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::candybot_vr::VisionMessage_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::candybot_vr::VisionMessage_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::candybot_vr::VisionMessage_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::candybot_vr::VisionMessage_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::candybot_vr::VisionMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "38c28f9d3b21cf8ed2fa3008fac27d63";
  }

  static const char* value(const ::candybot_vr::VisionMessage_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x38c28f9d3b21cf8eULL;
  static const uint64_t static_value2 = 0xd2fa3008fac27d63ULL;
};

template<class ContainerAllocator>
struct DataType< ::candybot_vr::VisionMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "candybot_vr/VisionMessage";
  }

  static const char* value(const ::candybot_vr::VisionMessage_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::candybot_vr::VisionMessage_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 face_count\n\
bool smile\n\
";
  }

  static const char* value(const ::candybot_vr::VisionMessage_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::candybot_vr::VisionMessage_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.face_count);
      stream.next(m.smile);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct VisionMessage_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::candybot_vr::VisionMessage_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::candybot_vr::VisionMessage_<ContainerAllocator>& v)
  {
    s << indent << "face_count: ";
    Printer<int32_t>::stream(s, indent + "  ", v.face_count);
    s << indent << "smile: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.smile);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CANDYBOT_VR_MESSAGE_VISIONMESSAGE_H
