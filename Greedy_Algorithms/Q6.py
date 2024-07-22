class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0
        for num_boxes, units_per_box in boxTypes:
            if truckSize >= num_boxes:
                total_units += num_boxes * units_per_box
                truckSize -= num_boxes
            else:
                total_units += truckSize * units_per_box
                break
        return total_units