import streamlit as st
import mysql.connector

# ==========================================
# PAGE CONFIGURATION & DECORATION
# ==========================================
st.set_page_config(page_title="EcoTrack System", page_icon="🌱", layout="wide")

# ==========================================
# DATABASE CONNECTION
# ==========================================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jenoshk@pereir@03022009", 
        database="EcoTrack"
    )

# ==========================================
# SIDEBAR NAVIGATION (8 OPTIONS)
# ==========================================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3299/3299935.png", width=100) # Cute eco icon
st.sidebar.title("🌱 EcoTrack Control")
st.sidebar.markdown("Track your waste, earn points, and help the environment!")
st.sidebar.divider()

menu = [
    "1. 🏠 Home / Dashboard",
    "2. ➕ Add New Student",
    "3. 📝 Add Waste Entry",
    "4. 📋 View All Logs",
    "5. 🏆 Individual Ranking",
    "6. 🏰 View House Totals",
    "7. 🔍 Search Student",
    "8. ❌ Remove Student"
]
choice = st.sidebar.radio("Select an option:", menu)

# ==========================================
# 1. HOME / DASHBOARD
# ==========================================
if choice == "1. 🏠 Home / Dashboard":
    st.title("Welcome to the EcoTrack System 🌱")
    st.markdown("### Use the sidebar on the left to navigate through the system.")
    st.info("💡 **Tip:** Make sure you register a student using 'Add New Student' before trying to log waste for them!")
    
    # Just a nice decorative element
    col1, col2, col3 = st.columns(3)
    col1.metric("Environment", "Protected", "100%")
    col2.metric("System Status", "Online", "Active")
    col3.metric("Database", "Connected", "EcoTrack")

# ==========================================
# 2. ADD NEW STUDENT
# ==========================================
elif choice == "2. ➕ Add New Student":
    st.title("➕ Register New Student")
    
    with st.form("add_student_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            s_id = st.text_input("Student ID")
            name = st.text_input("Student Name")
            house = st.selectbox("House", ["Red", "Blue", "Green", "Yellow", "Other"])
        with col2:
            grade = st.text_input("Grade (e.g., 10, 11, 12)")
            section = st.text_input("Section (e.g., A, B, C)")
            
        submitted = st.form_submit_button("Register Student")
        
        if submitted:
            if not s_id or not name:
                st.warning("Student ID and Name are required!")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    sql = "INSERT INTO Students (student_id, name, grade, section, house) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (s_id, name, grade, section, house))
                    conn.commit()
                    st.success(f"✅ Success! {name} (ID: {s_id}) has been added.")
                    st.balloons()
                except mysql.connector.Error as err:
                    st.error(f"Database error: {err}")
                finally:
                    if 'conn' in locals() and conn.is_connected():
                        cursor.close()
                        conn.close()

# ==========================================
# 3. ADD WASTE ENTRY
# ==========================================
elif choice == "3. 📝 Add Waste Entry":
    st.title("📝 Add Waste Entry")
    
    with st.form("add_waste_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            s_id = st.text_input("Student ID")
            w_type = st.selectbox("Waste Type", ["Plastic", "Paper", "Glass", "Metal", "Organic", "Other"])
        with col2:
            qty = st.number_input("Quantity", min_value=1, step=1)
            pts = st.number_input("Points Earned", min_value=0, step=1)
            
        submitted = st.form_submit_button("Submit Waste Log")
        
        if submitted:
            if not s_id:
                st.warning("Please enter a Student ID.")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    sql = "INSERT INTO WasteLog (student_id, waste_type, quantity, points_earned, collection_date) VALUES (%s, %s, %s, %s, CURDATE())"
                    cursor.execute(sql, (s_id, w_type, qty, pts))
                    conn.commit()
                    st.success(f"✅ Entry for Student {s_id} added successfully.")
                except mysql.connector.Error as err:
                    # Catching the exact error your CLI code caught
                    if err.errno == 1452:
                        st.error(f"❌ Error: Student ID '{s_id}' does not exist. Please add them in 'Add New Student' first.")
                    else:
                        st.error(f"Database error: {err}")
                finally:
                    if 'conn' in locals() and conn.is_connected():
                        cursor.close()
                        conn.close()

# ==========================================
# 4. VIEW ALL LOGS
# ==========================================
elif choice == "4. 📋 View All Logs":
    st.title("📋 Current Waste Logs")
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM WasteLog ORDER BY collection_date DESC")
        rows = cursor.fetchall()
        
        if rows:
            st.dataframe(rows, use_container_width=True)
        else:
            st.info("No logs found.")
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# ==========================================
# 5. INDIVIDUAL RANKING
# ==========================================
elif choice == "5. 🏆 Individual Ranking":
    st.title("🏆 Individual Ranking")
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT student_id, SUM(points_earned) as total FROM WasteLog GROUP BY student_id ORDER BY total DESC"
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            # Highlight top student
            st.subheader("🥇 Current Leader")
            st.metric(label=f"Student ID: {rows[0][0]}", value=f"{rows[0][1]} Points")
            st.divider()
            
            st.dataframe(rows, column_config={"0": "Student ID", "1": "Total Points"}, use_container_width=True)
        else:
            st.info("No rankings yet.")
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# ==========================================
# 6. VIEW HOUSE TOTALS
# ==========================================
elif choice == "6. 🏰 View House Totals":
    st.title("🏰 House-wise Totals")
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        SELECT s.house, SUM(w.points_earned) as total_points
        FROM Students s
        JOIN WasteLog w ON s.student_id = w.student_id
        GROUP BY s.house
        ORDER BY total_points DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        
        if rows:
            st.dataframe(rows, column_config={"0": "House Name", "1": "Total Points"}, use_container_width=True)
        else:
            st.info("No house points recorded yet.")
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

# ==========================================
# 7. SEARCH STUDENT
# ==========================================
elif choice == "7. 🔍 Search Student":
    st.title("🔍 Search Student")
    
    search_id = st.text_input("Enter Student ID to find:")
    if st.button("Search"):
        if search_id:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM Students WHERE student_id = %s", (search_id,))
                result = cursor.fetchone()
                
                if result:
                    st.success("Student Found!")
                    # Display results beautifully
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Name", result[1])
                    col2.metric("Grade & Section", f"{result[2]} - {result[3]}")
                    col3.metric("House", result[4])
                else:
                    st.warning("Student not found.")
            except mysql.connector.Error as err:
                st.error(f"Database error: {err}")
            finally:
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()

# ==========================================
# 8. REMOVE STUDENT
# ==========================================
elif choice == "8. ❌ Remove Student":
    st.title("❌ Remove Student")
    st.warning("Warning: This action cannot be undone.")
    
    del_id = st.text_input("Enter Student ID to remove:")
    
    if st.button("Delete Student", type="primary"):
        if del_id:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Students WHERE student_id = %s", (del_id,))
                conn.commit()
                
                if cursor.rowcount > 0:
                    st.success(f"✅ Student {del_id} removed from the system.")
                else:
                    st.info(f"Student ID {del_id} not found.")
                    
            except mysql.connector.Error as err:
                # Catching your exact Error 1451 from the original code!
                if err.errno == 1451:
                    st.error(f"❌ Error: Cannot delete student {del_id}.")
                    st.write("This student has existing waste logs. You must remove their logs in the database before deleting the student account.")
                else:
                    st.error(f"Database error: {err}")
            finally:
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()