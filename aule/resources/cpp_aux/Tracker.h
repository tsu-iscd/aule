#include <vector>

class Tracker_ {
public:
    template<typename T, typename ... Args>
    T* createInstance(Args&& ... args) {
//       static_assert(std::is_base_of<Node, T>::value, "Argument must be a Node derived type");
      T* result = new T(args...);
      _allocated.push_back(result);
      return result;
    }

    void reset() {
      for (auto entry : _allocated){
        delete entry;
      }
      _allocated.clear();
    }
    ~Tracker_(){ reset(); }

  private:
    std::vector<void *> _allocated;
};