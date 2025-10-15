class Patient:
    """Represents patient with a name and urgency level (1 = most urgent)."""
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

    def __repr__(self):
        return f"{self.name} ({self.urgency})"


class MinHeap:
    """Manages patients in priority queue based on urgency."""
    def __init__(self):
        self.data = []

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _heapify_up(self, index):
        """Restore heap order after insertion."""
        parent = (index - 1) // 2
        if index > 0 and self.data[index].urgency < self.data[parent].urgency:
            self._swap(index, parent)
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """Restore heap order after removal."""
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left
        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def insert(self, patient):
        """Add patient and reorder heap."""
        self.data.append(patient)
        self._heapify_up(len(self.data) - 1)

    def peek(self):
        """Return patient with highest priority (lowest urgency)."""
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        """Remove and return patient with the lowest urgency score."""
        if not self.data:
            return None
        self._swap(0, -1)
        min_patient = self.data.pop()
        if self.data:
            self._heapify_down(0)
        return min_patient

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")


# === Test Example ===
if __name__ == "__main__":
    heap = MinHeap()
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()

    next_up = heap.peek()
    print(f"\nNext Up: {next_up.name}, {next_up.urgency}\n")

    served = heap.remove_min()
    print(f"Served: {served.name}\n")
    heap.print_heap()


# Design Memo
# Why is a tree appropriate for the doctor structure?
#A tree is a good choice for the doctor structure because it naturally shows how one doctor can have others reporting to them. 
# Each doctor can have up to two reports, which makes it easy to build a hierarchy that looks like a real hospital organization chart. 
# Using a tree also makes it simple to add new doctors or look through the structure using traversal methods.

# When might a software engineer use preorder, inorder, or postorder traversals?
# Preorder, inorder, and postorder traversals each have different purposes. Preorder is useful when we want to visit the main doctor before checking their reports. 
# Inorder works well when we want to go through the structure in a certain order, like reading from left to right. 
# Postorder is helpful when we need to visit all the reports before the main doctor, such as when removing or evaluating parts of the tree.

# How do heaps help simulate real-time systems like emergency intake?
# Heaps are helpful for managing the emergency queue because they keep the most urgent patient at the top. 
# With a min-heap, the patient who needs care the fastest (one with lowest urgency number) is always first in line. 
# This makes it easy for hospitals or systems that deal with emergencies to handle patients in the right order without wasting time searching. 
# Overall, using trees and heaps helps organize data efficiently and shows how computer structures can solve real-world problems.