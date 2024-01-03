#geoms = ["rack", "palm", "cage", "thumb_base", "thumb_pf", "thumb_mf", "thumb_df", "ring_fingsup", "ring_pf", "ring_mf", "ring_df", "middle_fingsup", "middle_pf", "middle_mf", "middle_df", "index_fingsup", "index_pf", "index_mf", "index_df"]
geoms = ["palm_main", "palm_thumb", "palm_fingsup", "rack", "thumb_base", "thumb_motor", "finger_pf", "finger_mf", "finger_df"]

for i in geoms :
    for j in geoms :
        if i != j :
            print(f"<pair geom1=\""+i+"\" geom2=\""+j+"\"/>")