import math

class BiomechanicalEngine:
    def __init__(self, hip_coord, knee_coord, ankle_coord):
        """
        Initializes the engine with 2D spatial coordinates (x, y) 
        for the hip, knee, and ankle joints.
        """
        self.hip = hip_coord
        self.knee = knee_coord
        self.ankle = ankle_coord

    def _get_distance(self, p1, p2):
        """Calculates the Euclidean distance between two spatial points."""
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    def calculate_joint_angle(self):
        """
        Computes the absolute interior angle of the knee joint 
        using the Law of Cosines.
        """
        # Calculate lengths of the triangle sides (segment lengths)
        a = self._get_distance(self.knee, self.ankle)  # Shin segment length
        b = self._get_distance(self.hip, self.knee)    # Thigh segment length
        c = self._get_distance(self.hip, self.ankle)   # Distance from hip to ankle
        
        # Apply the Law of Cosines to find the interior angle at the knee
        try:
            cos_theta = (a**2 + b**2 - c**2) / (2 * a * b)
            
            # Clip values to stay within the valid arccos domain bounds [-1.0, 1.0]
            # This prevents math domain errors caused by minor floating-point variances
            cos_theta = max(-1.0, min(1.0, cos_theta))
            
            angle_rad = math.acos(cos_theta)
            return math.degrees(angle_rad)
            
        except ZeroDivisionError:
            # Safe boundary check to handle potential coordinate overlapping issues
            return 0.0

# Local verification block using sample joint coordinate entries
if __name__ == "__main__":
    print("--- Biomechanical Joint Analysis Engine Test Run ---")
    
    # Test case 1: Completely straight leg configuration
    # Hip(0, 10), Knee(0, 5), Ankle(0, 0) should equal a perfect 180.00 degree line
    straight_leg = BiomechanicalEngine((0, 10), (0, 5), (0, 0))
    print(f"Test 1 (Straight Leg Angle): {straight_leg.calculate_joint_angle():.2f}°")
    
    # Test case 2: Right angle leg flexion (90 degrees)
    # Hip(0, 5), Knee(0, 0), Ankle(5, 0) should equal a perfect 90.00 degree bend
    bent_leg = BiomechanicalEngine((0, 5), (0, 0), (5, 0))
    print(f"Test 2 (90-Degree Flexion Angle): {bent_leg.calculate_joint_angle():.2f}°")

