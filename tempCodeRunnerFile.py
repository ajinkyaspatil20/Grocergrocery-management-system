vsbp = ttk.Scrollbar(outputframe, orient="vertical", command=product_table.yview)
vsbp.pack(side="right", fill="y")
product_table.configure(yscrollcommand=vsbp.set)

hsbp = ttk.Scrollbar(outputframe, orient="horizontal", command=product_table.xview)
hsbp.pack(side="bottom", fill="x")
product_table.configure(xscrollcommand=hsbp.set)