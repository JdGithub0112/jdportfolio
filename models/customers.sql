-- Creating a CTE (Common Table Expression) named 'customers' to reference the 'stg_customers' table.
with customers as (
    select * from {{ ref('stg_customers') }}
),

-- Creating a CTE named 'orders' to reference the 'stg_orders' table.
orders as (
    select * from {{ ref('stg_orders') }}
),

-- Creating a CTE named 'customer_orders' to aggregate order data by customer.
customer_orders as (
    select
        customer_id, -- Selecting the customer ID

        -- Getting the earliest order date for each customer
        min(order_date) as first_order_date,
        
        -- Getting the most recent order date for each customer
        max(order_date) as most_recent_order_date,
        
        -- Counting the number of orders for each customer
        count(order_id) as number_of_orders

    from orders -- Using the 'orders' CTE as the source table

    group by 1 -- Grouping by the customer ID
),

-- Creating a CTE named 'final' to combine customer details with their order details.
final as (
    select
        customers.customer_id, -- Selecting the customer ID from the 'customers' CTE
        customers.first_name, -- Selecting the first name of the customer
        customers.last_name, -- Selecting the last name of the customer
        
        -- Joining with the 'customer_orders' CTE to get order details
        customer_orders.first_order_date,
        customer_orders.most_recent_order_date,
        
        -- Using COALESCE to ensure that if a customer has no orders, the count will be 0
        coalesce(customer_orders.number_of_orders, 0) as number_of_orders

    from customers -- Using the 'customers' CTE as the main source table

    -- Left joining with the 'customer_orders' CTE on the customer ID
    left join customer_orders using (customer_id)
)

-- Selecting all columns from the 'final' CTE to get the final result.
select * from final
