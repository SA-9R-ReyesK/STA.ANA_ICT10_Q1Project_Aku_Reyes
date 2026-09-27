# This part generates the SKU code from the selected shoe information
from pyscript import display, document

# This creates the final SKU from the selected information.
def SKU_generator(e):
    document.getElementById('sku_output').innerHTML = ""
    category = document.getElementById('category').value
    product_name = document.getElementById('product_name').value
    stock_qty = document.getElementById('quantity').value

    sku = category [ :3].upper() + "-" + product_name[ :4].upper() + "-" + stock_qty.zfill(4)

    display("SKU: ", sku, target='sku_output')

    def create_order(e):