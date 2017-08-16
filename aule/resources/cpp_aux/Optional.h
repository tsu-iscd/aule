#pragma once

#include <ostream>
#include <exception>
#include <typeinfo>
#include <string>

/* The `Optional` class is used to wrap non-nullable types
 * to give them this capability.
 */

class OptionalException : public std::exception {
    std::string value_type_name;
public:
    OptionalException(std::string vtn) {
        if(vtn == "i"){
            value_type_name = "int";}
        else if(vtn == "Ss"){
            value_type_name = "string";}
        else if(vtn == "b"){
            value_type_name = "bool";}
        else if(vtn == "d"){
            value_type_name = "double";}
        else{
            value_type_name = vtn;}
    };
    virtual const std::string what() {
        return "Trying to get value of uninitialized " + value_type_name;
    }
};

template <typename T>
class Optional{ /*CLASS DEFINITION BEGIN*/

    T value;
    bool initialized;

public:
    // For default arguments
    Optional(std::nullptr_t nullp = nullptr) : initialized(false){};

    Optional(const T& value_) : value(value_), initialized(true){};

    Optional operator=(const T& value_){
        value = value_;
        initialized = true;
        return *this;
    }

    Optional operator=(const Optional& other){
        initialized = other.initialized;
        if(initialized){
            value = other.value;
        }
        return *this;
    }

    T operator*(){
        if(initialized){
            return value;
        }
        else{
            throw OptionalException(typeid(T).name());;
        }
    }

    operator bool() const {
        return initialized;
    }

    void erase(){
        initialized = false;
    }

    std::string to_string(){
        return initialized ? string(value) : "null";
    }

    friend std::ostream& operator<<(std::ostream& out, Optional item){
        if(item.initialized){
            out << item.value;
        }
        else{
            out << "null";
        }
        return out;
    }
}; /*CLASS DEFINITION END*/