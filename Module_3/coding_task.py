import time
# try:
#     log_list = [
#         "[10:01:00] INFO: Server started",
#         "[10:01:03] INFO: Connection received",
#         "[10:01:05] WARNING: High memory usage",
#         "[10:01:06] ERROR: Database connection failed",
#         "[10:01:08] INFO: Retry attempt",
#         "[10:01:10] CRITICAL: Kernel panic detected",
#         "[10:01:12] INFO: Restarting service",
#         "[10:01:15] INFO: Initializing subsystem 'auth'",
#         "[10:01:18] INFO: Handshake established with node 04",
#         "[10:01:21] WARNING: Latency spike detected: 450ms",
#         "[10:01:23] INFO: Loading configuration from /etc/server.conf",
#         "[10:01:26] ERROR: SSL Certificate expired",
#         "[10:01:29] INFO: Requesting new certificate from CA",
#         "[10:01:31] INFO: Certificate updated successfully",
#         "[10:01:34] INFO: Connection received from 192.168.1.45",
#         "[10:01:37] WARNING: Disk space reaching 90% capacity",
#         "[10:01:40] INFO: Log rotation initiated",
#         "[10:01:43] INFO: User 'admin' logged in",
#         "[10:01:45] INFO: Cache cleared",
#         "[10:01:48] ERROR: Failed to write to socket",
#         "[10:01:50] INFO: Re-establishing socket connection",
#         "[10:01:53] INFO: Background worker started",
#         "[10:01:56] WARNING: Unoptimized query detected on table 'users'",
#         "[10:01:59] INFO: Indexing process completed",
#         "[10:02:01] INFO: Connection received from 10.0.0.12",
#         "[10:02:04] INFO: Health check passed",
#         "[10:02:07] INFO: Syncing data with backup server",
#         "[10:02:10] ERROR: Timeout waiting for response from API",
#         "[10:02:12] INFO: Retrying API request (1/3)",
#         "[10:02:15] INFO: API request successful",
#         "[10:02:18] WARNING: CPU temperature at 75C",
#         "[10:02:21] INFO: Fan speed increased to maximum",
#         "[10:02:24] INFO: Incoming packet rate: 1500 pkts/s",
#         "[10:02:27] CRITICAL: Unauthorized access attempt blocked",
#         "[10:02:30] INFO: IP address 203.0.113.5 blacklisted",
#         "[10:02:32] INFO: Loading module 'encryption'",
#         "[10:02:35] INFO: Encryption keys rotated",
#         "[10:02:38] INFO: Session 8842 timed out",
#         "[10:02:41] INFO: Garbage collection invoked",
#         "[10:02:44] WARNING: Deprecated API call used by client",
#         "[10:02:47] INFO: Server load average: 0.85",
#         "[10:02:49] INFO: Connection received from 172.16.25.4",
#         "[10:02:52] ERROR: Invalid JSON payload received",
#         "[10:02:55] INFO: Sending 400 Bad Request",
#         "[10:02:58] INFO: Database migration started",
#         "[10:03:01] INFO: Database migration completed successfully",
#         "[10:03:04] INFO: Service 'billing' is online",
#         "[10:03:07] WARNING: Potential memory leak in module 'web'",
#         "[10:03:10] INFO: Restarting worker process 1402",
#         "[10:03:13] INFO: Buffer size adjusted to 4096 bytes",
#         "[10:03:16] INFO: Monitoring agent connected",
#         "[10:03:19] INFO: Scheduled task 'cleanup' started",
#         "[10:03:21] INFO: 452 temporary files removed",
#         "[10:03:24] INFO: Scheduled task 'cleanup' finished",
#         "[10:03:27] ERROR: Failed to resolve hostname 'db.internal'",
#         "[10:03:30] INFO: Using cached IP for 'db.internal'",
#         "[10:03:33] WARNING: Slow I/O detected on mount /data",
#         "[10:03:36] INFO: Connection received from 192.168.1.102",
#         "[10:03:39] INFO: User 'guest' session started",
#         "[10:03:42] INFO: Compression enabled for outgoing traffic",
#         "[10:03:45] INFO: Firewall rules reloaded",
#         "[10:03:48] CRITICAL: Power supply failure on Unit 2",
#         "[10:03:51] INFO: Switched to redundant power supply",
#         "[10:03:54] INFO: System status: Operational (Degraded)",
#         "[10:03:57] WARNING: NTP sync offset > 100ms",
#         "[10:04:00] INFO: Resyncing system clock",
#         "[10:04:03] INFO: Clock synchronized",
#         "[10:04:06] INFO: API Key validation successful",
#         "[10:04:09] INFO: Transaction #9901 committed",
#         "[10:04:11] ERROR: Null pointer exception at line 442",
#         "[10:04:14] INFO: Generating crash dump",
#         "[10:04:17] INFO: Dump uploaded to developer portal",
#         "[10:04:20] INFO: Connection received from 8.8.8.8",
#         "[10:04:23] WARNING: Unusual traffic pattern detected",
#         "[10:04:26] INFO: Rate limiting applied to source IP",
#         "[10:04:29] INFO: Module 'analytics' initialized",
#         "[10:04:32] INFO: Heartbeat signal sent",
#         "[10:04:35] INFO: Heartbeat acknowledged by master",
#         "[10:04:38] ERROR: Read-only file system error",
#         "[10:04:41] INFO: Remounting /dev/sda1 as RW",
#         "[10:04:44] INFO: Mount successful",
#         "[10:04:47] INFO: Connection received from 192.168.1.15",
#         "[10:04:50] WARNING: Large file upload requested (2GB)",
#         "[10:04:53] INFO: Upload stream opened",
#         "[10:04:56] INFO: Upload completed (chunked)",
#         "[10:04:59] INFO: Checksum verification passed",
#         "[10:05:02] INFO: User 'dev_team' logged in",
#         "[10:05:05] INFO: Deployment script initiated",
#         "[10:05:08] INFO: Pulling latest changes from git",
#         "[10:05:11] INFO: Build process started",
#         "[10:05:14] INFO: Unit tests passed: 154/154",
#         "[10:05:17] INFO: Swapping production symlink",
#         "[10:05:20] INFO: Deployment successful",
#         "[10:05:23] WARNING: Zombie processes detected (3)",
#         "[10:05:26] INFO: Reaping child processes",
#         "[10:05:29] INFO: Connection received from 10.0.0.50",
#         "[10:05:32] ERROR: Out of file descriptors",
#         "[10:05:35] INFO: Ulimit increased for process",
#         "[10:05:38] INFO: System idle"
#     ]



#     for index, log in enumerate(log_list, start = 1):
#         if "INFO" in log:
#             continue
#         elif "ERROR" in log:
#             print(f"ERROR detected at line {index}: {log}")
#         elif "CRITICAL" in log:
#             print("\nCRITICAL FAILURE DETECTED\nShutting down monitoring system...")
#             break
#         else:
#             print(log)
#         time.sleep(1)
#     else:
#         print("System Healthy\nNo critical failures detected.")
# except KeyboardInterrupt:
#     print("\nMonitoring interrupted by user.\nSentinel shutting down safely.")



# efficiency_map.py


# inventory_data = [
#     ["PID-001", "Electronics", "In Stock", 45],
#     ["PID-002", "Home Decor", "Out of Stock", 0],
#     ["PID-003", "Apparel", "Low Stock", 5],
#     ["PID-004", "Electronics", "In Stock", 120],
#     ["PID-005", "Kitchenware", "Discontinued", 0],
#     ["PID-006", "Apparel", "In Stock", 88],
#     ["PID-007", "Toys", "In Stock", 200],
#     ["PID-008", "Electronics", "In Stock", 15],
#     ["PID-009", "Home Decor", "Low Stock", 3],
#     ["PID-010", "Books", "In Stock", 50],
#     ["PID-011", "Electronics", "Backorder", 0],
#     ["PID-012", "Office Supplies", "In Stock", 500],
#     ["PID-013", "Apparel", "In Stock", 64],
#     ["PID-014", "Toys", "In Stock", 12],
#     ["PID-015", "Kitchenware", "In Stock", 33],
#     ["PID-016", "Home Decor", "In Stock", 21],
#     ["PID-017", "Electronics", "Low Stock", 2],
#     ["PID-018", "Books", "In Stock", 110],
#     ["PID-019", "Apparel", "In Stock", 45],
#     ["PID-020", "Electronics", "In Stock", 30],
#     ["PID-021", "Office Supplies", "Low Stock", 8],
#     ["PID-022", "Kitchenware", "In Stock", 55],
#     ["PID-023", "Toys", "Out of Stock", 0],
#     ["PID-024", "Apparel", "In Stock", 140],
#     ["PID-025", "Home Decor", "In Stock", 19],
#     ["PID-026", "Electronics", "In Stock", 75],
#     ["PID-027", "Books", "Low Stock", 4],
#     ["PID-028", "Office Supplies", "In Stock", 250],
#     ["PID-029", "Apparel", "In Stock", 92],
#     ["PID-030", "Kitchenware", "In Stock", 18],
#     ["PID-031", "Electronics", "Discontinued", 0],
#     ["PID-032", "Toys", "In Stock", 60],
#     ["PID-033", "Home Decor", "In Stock", 33],
#     ["PID-034", "Books", "In Stock", 85],
#     ["PID-035", "Apparel", "Low Stock", 7],
#     ["PID-036", "Electronics", "In Stock", 42],
#     ["PID-037", "Office Supplies", "In Stock", 150],
#     ["PID-038", "Kitchenware", "In Stock", 29],
#     ["PID-039", "Toys", "Low Stock", 2],
#     ["PID-040", "Home Decor", "In Stock", 11],
#     ["PID-041", "Electronics", "In Stock", 88],
#     ["PID-042", "Apparel", "In Stock", 53],
#     ["PID-043", "Books", "Out of Stock", 0],
#     ["PID-044", "Office Supplies", "In Stock", 300],
#     ["PID-045", "Kitchenware", "In Stock", 47],
#     ["PID-046", "Electronics", "Low Stock", 9],
#     ["PID-047", "Toys", "In Stock", 125],
#     ["PID-048", "Home Decor", "In Stock", 25],
#     ["PID-049", "Apparel", "In Stock", 61],
#     ["PID-050", "Books", "In Stock", 200],
#     ["PID-051", "Office Supplies", "In Stock", 450],
#     ["PID-052", "Electronics", "In Stock", 34],
#     ["PID-053", "Kitchenware", "Low Stock", 3],
#     ["PID-054", "Toys", "In Stock", 80],
#     ["PID-055", "Home Decor", "In Stock", 44],
#     ["PID-056", "Apparel", "In Stock", 77],
#     ["PID-057", "Electronics", "Out of Stock", 0],
#     ["PID-058", "Books", "In Stock", 95],
#     ["PID-059", "Office Supplies", "In Stock", 120],
#     ["PID-060", "Kitchenware", "In Stock", 31],
#     ["PID-061", "Toys", "In Stock", 150],
#     ["PID-062", "Home Decor", "Low Stock", 6],
#     ["PID-063", "Apparel", "In Stock", 22],
#     ["PID-064", "Electronics", "In Stock", 110],
#     ["PID-065", "Books", "In Stock", 40],
#     ["PID-066", "Office Supplies", "Low Stock", 1],
#     ["PID-067", "Kitchenware", "In Stock", 66],
#     ["PID-068", "Toys", "In Stock", 19],
#     ["PID-069", "Home Decor", "In Stock", 37],
#     ["PID-070", "Apparel", "In Stock", 105],
#     ["PID-071", "Electronics", "In Stock", 59],
#     ["PID-072", "Books", "In Stock", 12],
#     ["PID-073", "Office Supplies", "In Stock", 85],
#     ["PID-074", "Kitchenware", "Out of Stock", 0],
#     ["PID-075", "Toys", "In Stock", 210],
#     ["PID-076", "Home Decor", "In Stock", 5],
#     ["PID-077", "Apparel", "In Stock", 33],
#     ["PID-078", "Electronics", "Low Stock", 8],
#     ["PID-079", "Books", "In Stock", 76],
#     ["PID-080", "Office Supplies", "In Stock", 225],
#     ["PID-081", "Kitchenware", "In Stock", 40],
#     ["PID-082", "Toys", "Low Stock", 4],
#     ["PID-083", "Home Decor", "In Stock", 18],
#     ["PID-084", "Apparel", "In Stock", 90],
#     ["PID-085", "Electronics", "In Stock", 100],
#     ["PID-086", "Books", "In Stock", 65],
#     ["PID-087", "Office Supplies", "In Stock", 50],
#     ["PID-088", "Kitchenware", "In Stock", 14],
#     ["PID-089", "Toys", "In Stock", 77],
#     ["PID-090", "Home Decor", "Out of Stock", 0],
#     ["PID-091", "Apparel", "In Stock", 48],
#     ["PID-092", "Electronics", "In Stock", 26],
#     ["PID-093", "Books", "Low Stock", 2],
#     ["PID-094", "Office Supplies", "In Stock", 135],
#     ["PID-095", "Kitchenware", "In Stock", 52],
#     ["PID-096", "Toys", "In Stock", 99],
#     ["PID-097", "Home Decor", "In Stock", 30],
#     ["PID-098", "Apparel", "In Stock", 115],
#     ["PID-099", "Electronics", "In Stock", 63],
#     ["PID-100", "Office Supplies", "In Stock", 410]
# ]
# start_time = time.perf_counter()
# search_term = "PID-3099"
# for data in inventory_data:
#     for sub_data in data:
#         if sub_data == search_term:
#             print(f"{search_term} Found!")
#             end_time = time.perf_counter()
#             print(f"Total Time taken = {end_time - start_time:0.4f} second/s")
#             break


inventory_dict = {
    "product_id": "PID-001",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 45,

    "product_id": "PID-002",
    "category": "Home Decor",
    "status": "Out of Stock",
    "stock": 0,

    "product_id": "PID-003",
    "category": "Apparel",
    "status": "Low Stock",
    "stock": 5,

    "product_id": "PID-004",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 120,

    "product_id": "PID-005",
    "category": "Kitchenware",
    "status": "Discontinued",
    "stock": 0,

    "product_id": "PID-006",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 88,

    "product_id": "PID-007",
    "category": "Toys",
    "status": "In Stock",
    "stock": 200,

    "product_id": "PID-008",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 15,

    "product_id": "PID-009",
    "category": "Home Decor",
    "status": "Low Stock",
    "stock": 3,

    "product_id": "PID-010",
    "category": "Books",
    "status": "In Stock",
    "stock": 50,

    "product_id": "PID-011",
    "category": "Electronics",
    "status": "Backorder",
    "stock": 0,

    "product_id": "PID-012",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 500,

    "product_id": "PID-013",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 64,

    "product_id": "PID-014",
    "category": "Toys",
    "status": "In Stock",
    "stock": 12,

    "product_id": "PID-015",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 33,

    "product_id": "PID-016",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 21,

    "product_id": "PID-017",
    "category": "Electronics",
    "status": "Low Stock",
    "stock": 2,

    "product_id": "PID-018",
    "category": "Books",
    "status": "In Stock",
    "stock": 110,

    "product_id": "PID-019",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 45,

    "product_id": "PID-020",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 30,

    "product_id": "PID-021",
    "category": "Office Supplies",
    "status": "Low Stock",
    "stock": 8,

    "product_id": "PID-022",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 55,

    "product_id": "PID-023",
    "category": "Toys",
    "status": "Out of Stock",
    "stock": 0,

    "product_id": "PID-024",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 140,

    "product_id": "PID-025",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 19,

    "product_id": "PID-026",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 75,

    "product_id": "PID-027",
    "category": "Books",
    "status": "Low Stock",
    "stock": 4,

    "product_id": "PID-028",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 250,

    "product_id": "PID-029",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 92,

    "product_id": "PID-030",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 18,

    "product_id": "PID-031",
    "category": "Electronics",
    "status": "Discontinued",
    "stock": 0,

    "product_id": "PID-032",
    "category": "Toys",
    "status": "In Stock",
    "stock": 60,

    "product_id": "PID-033",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 33,

    "product_id": "PID-034",
    "category": "Books",
    "status": "In Stock",
    "stock": 85,

    "product_id": "PID-035",
    "category": "Apparel",
    "status": "Low Stock",
    "stock": 7,

    "product_id": "PID-036",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 42,

    "product_id": "PID-037",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 150,

    "product_id": "PID-038",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 29,

    "product_id": "PID-039",
    "category": "Toys",
    "status": "Low Stock",
    "stock": 2,

    "product_id": "PID-040",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 11,

    "product_id": "PID-041",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 88,

    "product_id": "PID-042",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 53,

    "product_id": "PID-043",
    "category": "Books",
    "status": "Out of Stock",
    "stock": 0,

    "product_id": "PID-044",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 300,

    "product_id": "PID-045",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 47,

    "product_id": "PID-046",
    "category": "Electronics",
    "status": "Low Stock",
    "stock": 9,

    "product_id": "PID-047",
    "category": "Toys",
    "status": "In Stock",
    "stock": 125,

    "product_id": "PID-048",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 25,

    "product_id": "PID-049",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 61,

    "product_id": "PID-050",
    "category": "Books",
    "status": "In Stock",
    "stock": 200,

    "product_id": "PID-051",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 450,

    "product_id": "PID-052",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 34,

    "product_id": "PID-053",
    "category": "Kitchenware",
    "status": "Low Stock",
    "stock": 3,

    "product_id": "PID-054",
    "category": "Toys",
    "status": "In Stock",
    "stock": 80,

    "product_id": "PID-055",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 44,

    "product_id": "PID-056",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 77,

    "product_id": "PID-057",
    "category": "Electronics",
    "status": "Out of Stock",
    "stock": 0,

    "product_id": "PID-058",
    "category": "Books",
    "status": "In Stock",
    "stock": 95,

    "product_id": "PID-059",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 120,

    "product_id": "PID-060",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 31,

    "product_id": "PID-061",
    "category": "Toys",
    "status": "In Stock",
    "stock": 150,

    "product_id": "PID-062",
    "category": "Home Decor",
    "status": "Low Stock",
    "stock": 6,

    "product_id": "PID-063",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 22,

    "product_id": "PID-064",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 110,

    "product_id": "PID-065",
    "category": "Books",
    "status": "In Stock",
    "stock": 40,

    "product_id": "PID-066",
    "category": "Office Supplies",
    "status": "Low Stock",
    "stock": 1,

    "product_id": "PID-067",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 66,

    "product_id": "PID-068",
    "category": "Toys",
    "status": "In Stock",
    "stock": 19,

    "product_id": "PID-069",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 37,

    "product_id": "PID-070",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 105,

    "product_id": "PID-071",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 59,

    "product_id": "PID-072",
    "category": "Books",
    "status": "In Stock",
    "stock": 12,

    "product_id": "PID-073",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 85,

    "product_id": "PID-074",
    "category": "Kitchenware",
    "status": "Out of Stock",
    "stock": 0,

    "product_id": "PID-075",
    "category": "Toys",
    "status": "In Stock",
    "stock": 210,

    "product_id": "PID-076",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 5,

    "product_id": "PID-077",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 33,

    "product_id": "PID-078",
    "category": "Electronics",
    "status": "Low Stock",
    "stock": 8,

    "product_id": "PID-079",
    "category": "Books",
    "status": "In Stock",
    "stock": 76,

    "product_id": "PID-080",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 225,

    "product_id": "PID-081",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 40,

    "product_id": "PID-082",
    "category": "Toys",
    "status": "Low Stock",
    "stock": 4,

    "product_id": "PID-083",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 18,

    "product_id": "PID-084",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 90,

    "product_id": "PID-085",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 100,

    "product_id": "PID-086",
    "category": "Books",
    "status": "In Stock",
    "stock": 65,

    "product_id": "PID-087",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 50,

    "product_id": "PID-088",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 14,

    "product_id": "PID-089",
    "category": "Toys",
    "status": "In Stock",
    "stock": 77,

    "product_id": "PID-090",
    "category": "Home Decor",
    "status": "Out of Stock",
    "stock": 0,

    "product_id": "PID-091",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 48,

    "product_id": "PID-092",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 26,

    "product_id": "PID-093",
    "category": "Books",
    "status": "Low Stock",
    "stock": 2,

    "product_id": "PID-094",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 135,

    "product_id": "PID-095",
    "category": "Kitchenware",
    "status": "In Stock",
    "stock": 52,

    "product_id": "PID-096",
    "category": "Toys",
    "status": "In Stock",
    "stock": 99,

    "product_id": "PID-097",
    "category": "Home Decor",
    "status": "In Stock",
    "stock": 30,

    "product_id": "PID-098",
    "category": "Apparel",
    "status": "In Stock",
    "stock": 115,

    "product_id": "PID-099",
    "category": "Electronics",
    "status": "In Stock",
    "stock": 63,

    "product_id": "PID-100",
    "category": "Office Supplies",
    "status": "In Stock",
    "stock": 410,

}
search_term = "PID-100"
# print(f"{inventory_dict[]}")

if search_term in inventory_dict:
    print(f"{search_term} Found!")
else:
    print("Not Found")

print(inventory_dict["category"])