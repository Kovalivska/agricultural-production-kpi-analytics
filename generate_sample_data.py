"""
Generate synthetic production data for demonstration purposes
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_sample_production_data(n_days: int = 30) -> pd.DataFrame:
    """
    Generate synthetic production KPI data

    Args:
        n_days: Number of days of production data
    """
    np.random.seed(42)

    hours = n_days * 24
    timestamps = [datetime.now() - timedelta(hours=i) for i in range(hours)]
    timestamps.reverse()

    production_volume = np.random.randint(800, 1200, hours).astype(float)
    equipment_utilization = np.random.uniform(70, 95, hours)

    # Apply night shift effects
    for i in range(hours):
        hour_of_day = timestamps[i].hour
        if hour_of_day < 6 or hour_of_day > 22:
            production_volume[i] *= 0.7
            equipment_utilization[i] *= 0.8

    defect_rate_percent = np.random.uniform(0.5, 3.5, hours)
    quality_score = np.random.uniform(85, 98, hours)

    # Inject occasional quality issues
    issue_hours = np.random.choice(hours, size=int(hours * 0.1), replace=False)
    for i in issue_hours:
        defect_rate_percent[i] *= 2
        quality_score[i] *= 0.9

    data = {
        'timestamp': timestamps,
        'production_volume': production_volume,
        'production_rate': np.random.uniform(80, 120, hours),
        'cycle_time_minutes': np.random.uniform(2.5, 4.5, hours),
        'quality_score': quality_score,
        'defect_rate_percent': defect_rate_percent,
        'first_pass_yield': np.random.uniform(92, 99, hours),
        'equipment_utilization': equipment_utilization,
        'downtime_minutes': np.random.randint(0, 45, hours),
        'oee_score': np.random.uniform(65, 90, hours),
        'material_waste_percent': np.random.uniform(2, 8, hours),
        'energy_kwh': np.random.uniform(150, 250, hours),
        'labor_hours': np.random.uniform(4, 8, hours),
        'production_cost_per_unit': np.random.uniform(1.8, 2.5, hours),
        'total_cost': np.random.uniform(1800, 2800, hours),
    }

    df = pd.DataFrame(data)
    df['efficiency_score'] = df['equipment_utilization'] * df['quality_score'] / 100
    df['waste_cost'] = (df['material_waste_percent'] / 100) * df['total_cost']

    output_path = 'data/sample_production_data.csv'
    import os
    os.makedirs('data', exist_ok=True)
    df.to_csv(output_path, index=False)

    print("✅ Sample production data created:")
    print(f"   - File: {output_path}")
    print(f"   - Days: {n_days}")
    print(f"   - Hours: {hours}")
    print(f"   - Metrics: {len(df.columns)}")
    print(f"   - Size: {df.memory_usage(deep=True).sum() / 1024:.1f} KB")

    print("\n📊 Data Summary:")
    print(f"   - Avg Production: {df['production_volume'].mean():.0f} units/hour")
    print(f"   - Avg Quality Score: {df['quality_score'].mean():.1f}%")
    print(f"   - Avg Defect Rate: {df['defect_rate_percent'].mean():.2f}%")
    print(f"   - Avg Equipment Utilization: {df['equipment_utilization'].mean():.1f}%")

    return df


if __name__ == "__main__":
    generate_sample_production_data(n_days=30)
    print("\n✅ Sample data generation complete!")
