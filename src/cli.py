from pathlib import Path

def update():
    # Step 1에서 Typer/Hydra로 파이프라인 엔트리포인트를 구성합니다.
    data_dir = Path("data")
    (data_dir / "processed").mkdir(parents=True, exist_ok=True)
    print("Pipeline stub: coming in Step 1.")

if __name__ == "__main__":
    update()
