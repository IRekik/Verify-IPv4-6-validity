class Solution:
    def is_valid_IPv6_segment(self, segment: str) -> bool:
        """Verify if IPv6 segment is valid
        Args:
            segment(str): the IPv6 string segment to analyze
        Returns:
            A boolean to determine if segment is a valid IPv6 segment or not
        """
        valid_chars = "1234567890abcdefABCDEF"
        for c in segment:
            if c not in valid_chars:
                return False
        return True

    def is_IPv4(self, query_IP: str) -> bool:
        """Determine if IP address proposition is a valid IPv4
        Args:
            query_IP(str): the proposed IP address
        Returns:
            A boolean to determine if segment is a valid IPv4 address or not
        """
        if "." not in query_IP:
            return False
        IP_segments_list = query_IP.split(".")
        if len(IP_segments_list) != 4:
            return False
        # For each ip segment, check if segment is only digits, is between
        # 0 and 255 and has no leading zero
        for i in IP_segments_list:
            if not i.isdigit():
                return False
            if int(i) < 0 or int(i) > 255:
                return False
            if len(i) > 1 and i[0] == "0":
                return False
        return True

    def is_IPv6(self, query_IP: str) -> bool:
        """Determine if IP address proposition is a valid IPv4
        Args:
            query_IP(str): the proposed IP address
        Returns:
            A boolean to determine if segment is a valid IPv4 address or not
        """
        if ":" not in query_IP:
            return False
        IP_segments_list = query_IP.split(":")
        if len(IP_segments_list) != 8:
            return False
        # For each ip segment, check that segment has between
        # 1 and 4 characters and is a valid segment
        for i in IP_segments_list:
            if len(i) == 0 or len(i) > 4:
                return False
            if not self.is_valid_IPv6_segment(i):
                return False
        return True

    def valid_IP_address(self, query_IP: str) -> str:
        """Determine if IP address proposition is a valid IPv4 or IPv6
        Args:
            query_IP(str): the proposed IP address
        Returns:
            A string that is either "IPv4", "IPv6" or "Neither"
        """
        if self.is_IPv4(query_IP):
            return "IPv4"
        if self.is_IPv6(query_IP):
            return "IPv6"
        return "Neither"


IP = "172.16.254.1"
print(Solution().valid_IP_address(IP))
