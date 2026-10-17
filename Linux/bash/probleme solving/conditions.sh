read x

if [[ "${x,,}" == "y" ]]; then 
    echo "YES" 
elif [[ "${x,,}" == "n" ]]; then 
    echo "NO" 
fi
